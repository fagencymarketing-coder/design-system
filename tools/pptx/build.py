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
DY=float(os.environ.get('DY','0'))   # калибровка по вертикали, px

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

def add_text(slide,t,idx):
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
    width=max(l['right'] for l in lines)-left+20
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
            r.font.color.rgb=RGBColor(cr,cg,cb)
            rPr=r._r.get_or_add_rPr()
            set_alpha(rPr.find(qn('a:solidFill')),ca)
            if st.get('ls'): rPr.set('spc',str(int(round(st['ls']*0.75*100))))
            if st.get('tt')=='uppercase': rPr.set('cap','all')
            # кириллица и латиница одним шрифтом
            for tag in ('a:ea','a:cs'):
                el=etree.SubElement(rPr,qn(tag)); el.set('typeface',fam)
    return tb

def build(names,dst):
    data=json.load(open(os.path.join(OUT,'layouts-data.json'),encoding='utf8'))
    prs=Presentation(); prs.slide_width=Emu(1080*PX); prs.slide_height=Emu(1080*PX)
    blank=prs.slide_layouts[6]
    for name in names:
        d=data[name]; s=prs.slides.add_slide(blank)
        s.name=name
        pic=s.shapes.add_picture(os.path.join(OUT,name+'-bg.png'),0,0,Emu(1080*PX),Emu(1080*PX)); pic.name='Фон (картинка, без текста)'
        for im in d['imgs']:
            path=unquote(urlparse(im['src']).path)
            p=s.shapes.add_picture(path,Emu(int(im['x']*PX)),Emu(int(im['y']*PX)),Emu(int(im['w']*PX)),Emu(int(im['h']*PX)))
            p.name='Логотип' if im['logo'] else 'Фото / вырезка'
        for i,dh in enumerate(d['dashes']): add_rect(s,dh['x'],dh['y'],dh['w'],dh['h'],dh['color'],'Малиновая черта')
        for i,t in enumerate(d['texts']): add_text(s,t,i+1)
        # заметки
        s.notes_slide.notes_text_frame.text='Шрифт Gilroy. Текст редактируется; фон (фото, паттерн, значки) лежит одной картинкой, логотип и вырезки отдельно.'
    prs.save(dst)

if __name__=='__main__':
    names=sys.argv[2:] or [k for k in json.load(open(os.path.join(OUT,'layouts-data.json'),encoding='utf8'))]
    build(names,sys.argv[1])
    print('saved',sys.argv[1],len(names))
