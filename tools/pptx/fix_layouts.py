"""Раскладка слайдов: «Blank» остаётся чистой, а плейсхолдеры фото/иконки живут в отдельной раскладке «Фото-слоты»,
которую получают только слайды с заглушками. Пустые плейсхолдеры на слайдах удаляются."""
import copy
from lxml import etree
from pptx.opc.constants import RELATIONSHIP_TYPE as RT, CONTENT_TYPE as CT
from pptx.opc.packuri import PackURI
from pptx.oxml.ns import qn
from pptx.parts.slide import SlideLayoutPart

NEW='Фото-слоты'

def _is_slot_ph(el):
    ph=el.find('.//'+qn('p:ph'))
    return ph is not None and ph.get('type')=='pic' and ph.get('idx') in ('10','11')

def fix_layouts(prs):
    blank=[l for l in prs.slide_layouts if l.name=='Blank'][0]
    new=[l for l in prs.slide_layouts if l.name==NEW]
    if new: new_layout=new[0]
    else:
        # собрать плейсхолдеры из Blank (или создать), убрать из Blank
        tree=blank.shapes._spTree
        phs=[sp for sp in tree.findall(qn('p:sp')) if _is_slot_ph(sp)]
        blob=etree.tostring(blank._element,xml_declaration=True,encoding='UTF-8',standalone=True)
        pkg=prs.part.package
        import re
        n=1+max(int(re.search(r'slideLayout(\d+)\.xml$',str(p.partname)).group(1)) for p in pkg.iter_parts() if re.search(r'slideLayout\d+\.xml$',str(p.partname)))
        part=SlideLayoutPart.load(PackURI('/ppt/slideLayouts/slideLayout%d.xml'%n),CT.PML_SLIDE_LAYOUT,pkg,blob)
        part.relate_to(prs.slide_master.part,RT.SLIDE_MASTER)
        rid=prs.slide_master.part.relate_to(part,RT.SLIDE_LAYOUT)
        lst=prs.slide_master._element.find(qn('p:sldLayoutIdLst'))
        ids=[int(e.get('id')) for e in lst]+[int(prs.slide_master._element.get('id','0') or 0)]
        e=etree.SubElement(lst,qn('p:sldLayoutId')); e.set('id',str(max(ids+[2147483648])+1)); e.set(qn('r:id'),rid)
        new_layout=[l for l in prs.slide_layouts if l.part is part][0]
        new_layout._element.find(qn('p:cSld')).set('name',NEW)
        # в новой раскладке — плейсхолдеры: убрать все sp-плейсхолдеры, кроме слотов (если их не было — создать)
        t2=new_layout.shapes._spTree
        for sp in list(t2.findall(qn('p:sp'))):
            if not _is_slot_ph(sp): t2.remove(sp)
        if not any(_is_slot_ph(sp) for sp in t2.findall(qn('p:sp'))):
            for sp in phs: t2.append(copy.deepcopy(sp))
        for sp in phs: tree.remove(sp)
    # убрать слоты из Blank, если остались
    tree=blank.shapes._spTree
    for sp in list(tree.findall(qn('p:sp'))):
        if _is_slot_ph(sp): tree.remove(sp)
    # слайды
    for s in prs.slides:
        t=s.shapes._spTree
        has_slot=any(_is_slot_ph(e) for e in t.findall(qn('p:pic')))
        for sp in list(t.findall(qn('p:sp'))):          # пустые плейсхолдеры
            if _is_slot_ph(sp): t.remove(sp)
        if has_slot:
            for rel in s.part.rels.values():
                if rel.reltype==RT.SLIDE_LAYOUT: rel._target=new_layout.part
        else:
            for rel in s.part.rels.values():
                if rel.reltype==RT.SLIDE_LAYOUT: rel._target=blank.part
