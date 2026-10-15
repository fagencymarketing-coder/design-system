"""Собирает редактируемый PPTX из извлечённых данных макетов.
Слайд 1080×1080 px (1 px = 9525 EMU). Слои: фон (картинка), логотип/фото, чёрточки, текст (Gilroy)."""
import json, os, re, sys
from urllib.parse import unquote, urlparse
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'out')
PX=9525
DY=float(os.environ.get('DY','0'))
FISH=json.load(open(os.path.join(HERE,'fish.json'),encoding='utf8'))   # калибровка по вертикали, px

FONTS={300:('Gilroy Light',False),400:('Gilroy',False),500:('Gilroy Medium',False),600:('Gilroy SemiBold',False),
       700:('Gilroy',True),800:('Gilroy ExtraBold',False),900:('Gilroy ExtraBold',False)}

def parse_color(s):
    m=re.match(r'rgba?\(([^)]+)\)',s)
    p=[float(x) for x in m.group(1).replace('/',',').split(',')]
    a=p[3] if len(p)>3 else 1.0
    return int(p[0]),int(p[1]),int(p[2]),a

def set_alpha(color_fmt_elm_parent, a):
    if a>=0.999: return
    clr=color_fmt_elm_parent.find('.//'+qn('a:srgbClr'))
    al=etree.SubElement(clr,qn('a:alpha')); al.set('val',str(int(a*100000)))

def add_rect(slide,x,y,w,h,color,name):
    r,g,b,a=parse_color(color)
    sp=slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,Emu(int(x*PX)),Emu(int(y*PX)),Emu(int(w*PX)),Emu(int(h*PX)))
    sp.fill.solid(); sp.fill.fore_color.rgb=RGBColor(r,g,b); sp.line.fill.background(); sp.name=name
    sp.shadow.inherit=False
    return sp

def apply_fish(t,fl):
    """Заменяет текст блока на рыбу, сохраняя стили: *слово* = акцентный стиль блока."""
    base=t['lines'][0]['runs'][0]['st']; acc=None
    for l in t['lines']:
        for r in l['runs']:
            if r['st']!=base: acc=r['st']; break
        if acc: break
    acc=acc or base
    new=[]
    for i,txt in enumerate(fl):
        src=t['lines'][min(i,len(t['lines'])-1)]
        runs=[]
        for j,part in enumerate(txt.split('*')):
            if part: runs.append({'text':part,'st':acc if j%2 else base})
        new.append({'top':src['top'],'bottom':src['bottom'],'left':src['left'],'right':src['right'],'runs':runs})
    t=dict(t); t['lines']=new; return t

def add_text(slide,t,idx,bgim=None):
    if t.get('marker'):
        lines=[{'top':t['y'],'left':t['x'],'right':t['x']+40,'bottom':t['y']+t['size'],
                'runs':[{'text':t['text'],'st':{'color':t['color'],'weight':t['weight'],'size':t['size'],'ls':0,'tt':'none'}}]}]
        lh=t['size']*1.0; size=t['size']; tt='none'; name='Маркер списка'
    else:
        lines=t['lines']; lh=t['lh']; size=t['size']; tt=t['tt']; name='Текст %d'%idx
    first=lines[0]
    fh=first['bottom']-first['top']
    top=first['top']-(lh-fh)/2+DY+0.24*max(0,size-lh)   # крупный кегль с плотным интерлиньяжем: LibreOffice/PowerPoint сдвигают вверх
    left=min(l['left'] for l in lines)
    width=max(max(l['right'] for l in lines)-left+20, 1080-left-24)   # запас по ширине под длинный текст
    height=lh*len(lines)
    tb=slide.shapes.add_textbox(Emu(int(left*PX)),Emu(int(top*PX)),Emu(int(width*PX)),Emu(int(height*PX)))
    tb.name=name
    tf=tb.text_frame; tf.word_wrap=False
    tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=0
    tf.vertical_anchor=MSO_ANCHOR.TOP
    bp=tf._txBody.find(qn('a:bodyPr'))
    for ch in list(bp): bp.remove(ch)          # без автоподбора размера
    p=tf.paragraphs[0]; p.alignment=PP_ALIGN.LEFT
    p.line_spacing=Pt(lh*0.75)
    for li,l in enumerate(lines):
        if li>0: p.add_line_break()
        for run in l['runs']:
            if not run['text']: continue
            st=run['st']; r=p.add_run(); r.text=run['text']
            fam,bold=FONTS.get(st['weight'],('Gilroy',False))
            r.font.name=fam; r.font.bold=bold; r.font.size=Pt(st['size']*0.75)
            cr,cg,cb,ca=parse_color(st['color'])
            if ca<0.999 and bgim is not None:      # полупрозрачный текст -> сплошной цвет, смешанный с фоном (стабильнее в PowerPoint)
                bx=int(min(1079,max(0,l['left']+4))); by=int(min(1079,max(0,(l['top']+l['bottom'])/2)))
                br,bg_,bb,ba=bgim.getpixel((bx,by))
                if ba>250:
                    cr=int(cr*ca+br*(1-ca)); cg=int(cg*ca+bg_*(1-ca)); cb=int(cb*ca+bb*(1-ca)); ca=1.0
            r.font.color.rgb=RGBColor(cr,cg,cb)
            rPr=r._r.get_or_add_rPr()
            set_alpha(rPr.find(qn('a:solidFill')),ca)
            if st.get('ls'): rPr.set('spc',str(int(round(st['ls']*0.75*100))))
            if st.get('tt')=='uppercase': rPr.set('cap','all')
            # кириллица и латиница одним шрифтом
            for tag in ('a:ea','a:cs'):
                el=etree.SubElement(rPr,qn(tag)); el.set('typeface',fam)
    return tb


from PIL import Image, ImageEnhance
def _ph(pic,idx):
    nvPr=pic._element.nvPicPr.nvPr
    ph=etree.SubElement(nvPr,qn('p:ph')); ph.set('type','pic'); ph.set('idx',str(idx))

def add_slot_picture(slide,path,x,y,w,h,idx,name,crop=None,radius=0):
    pic=slide.shapes.add_picture(path,Emu(int(x*PX)),Emu(int(y*PX)),Emu(int(w*PX)),Emu(int(h*PX)))
    pic.name=name; _ph(pic,idx)
    if crop: pic.crop_left,pic.crop_top,pic.crop_right,pic.crop_bottom=crop
    if radius:
        geom=pic._element.spPr.find(qn('a:prstGeom')); geom.set('prst','roundRect')
        av=geom.find(qn('a:avLst'))
        if av is None: av=etree.SubElement(geom,qn('a:avLst'))
        gd=etree.SubElement(av,qn('a:gd')); gd.set('name','adj'); gd.set('fmla','val %d'%int(radius/min(w,h)*100000))
    return pic

def cover_crop(iw,ih,w,h,pos):
    sc=max(w/iw,h/ih); vw,vh=w/sc,h/sc
    px,py=[float(p.strip('%'))/100 for p in pos.split()]
    l=(iw-vw)*px; t=(ih-vh)*py
    return (l/iw,t/ih,(iw-vw-l)/iw,(ih-vh-t)/ih)

def add_layout_placeholders(prs):
    lay=prs.slide_layouts[6]
    tree=lay.shapes._spTree
    for idx,nm,prompt in ((10,'Фото','Щёлкните значок, чтобы добавить фото'),(11,'Иконка','Щёлкните значок, чтобы добавить иконку')):
        xml=('<p:sp xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
             '<p:nvSpPr><p:cNvPr id="%d" name="%s"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="pic" idx="%d"/></p:nvPr></p:nvSpPr>'
             '<p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm></p:spPr>'
             '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="ru-RU"/><a:t>%s</a:t></a:r></a:p></p:txBody></p:sp>')%(30+idx,nm,idx,300*PX,300*PX,prompt)
        tree.append(etree.fromstring(xml))

def build(names,dst):
    data=json.load(open(os.path.join(OUT,'layouts-data.json'),encoding='utf8'))
    prs=Presentation(); prs.slide_width=Emu(1080*PX); prs.slide_height=Emu(1080*PX)
    add_layout_placeholders(prs)
    blank=prs.slide_layouts[6]
    for name in names:
        d=data[name]; s=prs.slides.add_slide(blank)
        fish=FISH.get(name,{})
        s.name=name
        bgpath=os.path.join(OUT,name+'-bg.png')
        slots=d.get('slots',[])
        fade=[sl for sl in slots if sl.get('fade')]
        if fade:   # плавный переход фона в фото: полупрозрачный верх фонового слоя
            im=Image.open(bgpath).convert('RGBA'); a=im.split()[3]; px=a.load()
            f=fade[0]['fade']['h']; y0=int(fade[0]['y'])
            for yy in range(y0,1080):
                k=max(0.0,1-(yy-y0)/f)
                for xx in range(1080): px[xx,yy]=int(px[xx,yy]*k)
            im.putalpha(a); bgpath=os.path.join(OUT,name+'-bg-fade.png'); im.save(bgpath)
        def put_slots(before):
            for sl in slots:
                if bool(sl.get('fade'))!=before: continue
                if sl['kind']=='photo':
                    src=unquote(urlparse(sl['src']).path); img=Image.open(src); iw,ih=img.size
                    if sl.get('saturate'):
                        img=ImageEnhance.Color(img.convert('RGB')).enhance(sl['saturate']); src=os.path.join(OUT,name+'-photo.jpg'); img.save(src,quality=92)
                    add_slot_picture(s,src,sl['x'],sl['y'],sl['w'],sl['h'],10,sl['name']+' (заменить: Изменить рисунок)',cover_crop(iw,ih,sl['w'],sl['h'],sl['pos']),sl.get('radius',0))
                elif sl['kind']=='icon' and sl.get('png'):
                    add_slot_picture(s,sl['png'],sl['x'],sl['y'],sl['w'],sl['h'],11,sl['name']+' (заменить: Изменить рисунок)')
        bgim=Image.open(bgpath).convert('RGBA')
        put_slots(True)
        pic=s.shapes.add_picture(bgpath,0,0,Emu(1080*PX),Emu(1080*PX)); pic.name='Фон (картинка, без текста)'
        put_slots(False)
        for im in d['imgs']:
            path=unquote(urlparse(im['src']).path)
            if im['logo']:
                p=s.shapes.add_picture(path,Emu(int(im['x']*PX)),Emu(int(im['y']*PX)),Emu(int(im['w']*PX)),Emu(int(im['h']*PX))); p.name='Логотип'
            else:
                add_slot_picture(s,path,im['x'],im['y'],im['w'],im['h'],10,'Фото сотрудника, вырезка PNG (заменить: Изменить рисунок)')
        for i,dh in enumerate(d['dashes']): add_rect(s,dh['x'],dh['y'],dh['w'],dh['h'],dh['color'],'Малиновая черта')
        for i,t in enumerate(d['texts']):
            if not t.get('marker') and str(i) in fish: t=apply_fish(t,fish[str(i)])
            add_text(s,t,i+1,bgim)
        # заметки
        s.notes_slide.notes_text_frame.text='Шаблон. Текст-«рыба» заменяется своим. Фото и иконки: выделить, правая кнопка → Изменить рисунок. Шрифт Gilroy встроен в файл.'
    prs.save(dst)


def embed_fonts(path):
    """Встраивает Gilroy (EOT .fntdata) в PPTX: PowerPoint берёт шрифт из файла, если он не установлен."""
    import zipfile, shutil
    EOT=os.path.join(OUT,'eot')
    fams=[('Gilroy Light',{'regular':'Light'}),('Gilroy',{'regular':'Regular','bold':'Bold'}),('Gilroy Medium',{'regular':'Medium'}),
          ('Gilroy SemiBold',{'regular':'Semibold'}),('Gilroy ExtraBold',{'regular':'Extrabold'})]
    zin=zipfile.ZipFile(path); items=[(i,zin.read(i.filename)) for i in zin.infolist()]; zin.close()
    files={i.filename:d for i,d in items}
    rels=files['ppt/_rels/presentation.xml.rels'].decode('utf8')
    pres=files['ppt/presentation.xml'].decode('utf8')
    ct=files['[Content_Types].xml'].decode('utf8')
    lst='<p:embeddedFontLst>'; n=0; newfiles={}
    for fam,styles in fams:
        lst+='<p:embeddedFont><p:font typeface="%s"/>'%fam
        for st,fn in styles.items():
            n+=1; rid='rIdFont%d'%n; part='fonts/font%d.fntdata'%n
            newfiles['ppt/'+part]=open(os.path.join(EOT,fn+'.eot'),'rb').read()
            rels=rels.replace('</Relationships>','<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/font" Target="%s"/></Relationships>'%(rid,part))
            lst+='<p:%s r:id="%s"/>'%(st,rid)
        lst+='</p:embeddedFont>'
    lst+='</p:embeddedFontLst>'
    pres=re.sub(r'(<p:notesSz[^>]*/>)',lambda m:m.group(1)+lst,pres,count=1)
    if 'embedTrueTypeFonts' not in pres: pres=pres.replace('<p:presentation ','<p:presentation embedTrueTypeFonts="1" ',1)
    if 'saveSubsetFonts' not in pres: pres=pres.replace('<p:presentation ','<p:presentation saveSubsetFonts="1" ',1)
    if 'Extension="fntdata"' not in ct:
        ct=ct.replace('<Default ','<Default Extension="fntdata" ContentType="application/x-fontdata"/><Default ',1)
    files['ppt/_rels/presentation.xml.rels']=rels.encode('utf8'); files['ppt/presentation.xml']=pres.encode('utf8'); files['[Content_Types].xml']=ct.encode('utf8')
    tmp=path+'.tmp'
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as zo:
        for i,d in items: zo.writestr(i.filename,files[i.filename])
        for k,v in newfiles.items(): zo.writestr(k,v)
    shutil.move(tmp,path)

if __name__=='__main__':
    names=sys.argv[2:] or [k for k in json.load(open(os.path.join(OUT,'layouts-data.json'),encoding='utf8'))]
    build(names,sys.argv[1])
    embed_fonts(sys.argv[1])
    print('saved',sys.argv[1],len(names))
