#!/usr/bin/env python3
"""Квадрат с продлённой стеной под заголовок. python3 tools/make-square.py <кадр.jpg> <выход.jpg> <y0> <ext>
 y0 — строка (при ширине 1080), с которой начинается фото, выше — чистая стена; ext — высота продления сверху."""
import sys, numpy as np
from PIL import Image, ImageFilter, ImageOps
W=1080
def smooth(v,k=91):
    pad=k//2; vp=np.pad(v,((pad,pad),(0,0)),mode='edge'); ker=np.ones(k)/k
    return np.stack([np.convolve(vp[:,c],ker,mode='valid') for c in range(3)],1)
def build(src,dst,y0,ext):
    im=Image.open(src).convert('RGB'); p=im.resize((W,int(im.height*W/im.width)),Image.LANCZOS)
    S=p.crop((0,0,W,y0)); fl=ImageOps.flip(S); stack=Image.new('RGB',(W,ext)); y=ext
    for piece in [fl,S]*6:
        y-=piece.height; stack.paste(piece,(0,y))
        if y<=0: break
    c=Image.new('RGB',(W,W)); c.paste(stack,(0,0)); c.paste(p.crop((0,y0,W,y0+W-ext)),(0,ext))
    a=np.asarray(c).astype(np.float32); seam=ext
    up=smooth(a[seam-14:seam-2].mean(0)); dn=smooth(a[seam+2:seam+14].mean(0)); r=dn/np.maximum(up,1)
    w=np.clip(1-(seam-np.arange(W))/420.0,0,1)
    a[:seam]=a[:seam]*(r[None,:,:]**w[:seam,None,None])
    out=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    out.paste(out.crop((0,seam-8,W,seam+8)).filter(ImageFilter.GaussianBlur(1.6)),(0,seam-8))
    out.save(dst,quality=92)
if __name__=='__main__': build(sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
