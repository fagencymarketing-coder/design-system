"""Правки в файле, который редактирует заказчик: сохраняет её тексты и изменения, применяет только то, что просили.
Использование: python3 patch_user_file.py in.pptx out.pptx"""
import sys, os, io
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from pptx import Presentation
from pptx.util import Emu
from fix_layouts import fix_layouts

def replace_bg(slide,png):
    for sh in slide.shapes:
        if sh.name.startswith('Фон'):
            old=sh._element.blipFill.find('{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
            img_part,rId=slide.part.get_or_add_image_part(png)
            old.set('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed',rId)
            return True
    return False

if __name__=='__main__':
    src,dst=sys.argv[1],sys.argv[2]
    prs=Presentation(src)
    out=os.path.join(HERE,'out')
    for s in prs.slides:
        if s.name.startswith('U6-urgent-ticker'):
            ok=replace_bg(s,os.path.join(out,'U6-urgent-ticker-green-bg.png')); s.name='U6-urgent-ticker-green'; print('U6 фон заменён:',ok)
    fix_layouts(prs)
    prs.save(dst)
