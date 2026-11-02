def page(W,H,P):
    return f"""<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><style>
@font-face{{font-family:'Manrope';src:url('Manrope-Variable.ttf');font-weight:200 800}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px}}
body{{position:relative;overflow:hidden;background:linear-gradient(180deg,#e7e7ee,#fff 62%);font-family:'Manrope',sans-serif}}
.blob{{position:absolute;border-radius:50%;background:linear-gradient(135deg,rgba(136,153,235,.30),rgba(113,96,163,.22));left:{P['bx']}px;top:{P['by']}px;width:{P['bd']}px;height:{P['bd']}px}}
.blob2{{position:absolute;border-radius:50%;background:#d6001f;left:{P['b2x']}px;top:{P['b2y']}px;width:{P['b2d']}px;height:{P['b2d']}px}}
.logo{{position:absolute;left:{P['m']}px;top:{P['ly']}px;width:{P['lw']}px}}
.ln{{position:absolute;left:{P['m']}px;top:{P['ly']+int(P['lw']*0.62)+20}px;width:64px;height:5px;background:#d6001f}}
.h{{position:absolute;left:{P['m']}px;right:{P['m']}px;top:{P['hy']}px;font-weight:800;color:#1b1b2b;font-size:{P['hs']}px;line-height:1.08;letter-spacing:-.025em}}
.pill{{color:#d6001f}}
.h .q{{display:block;color:#7160a3;margin-top:.22em}}
.card{{position:absolute;left:{P['cx']}px;top:{P['cy']}px;width:{P['cw']}px;height:{P['ch']}px;background:#fff;border-radius:56px;box-shadow:0 18px 50px rgba(80,60,150,.14);display:flex;align-items:center;justify-content:center}}
.card img{{width:{P['tw']}px}}
.st{{position:absolute;width:{P['sw']}px}}
.env{{position:absolute;width:{P['ew']}px;left:{P['ex']}px;top:{P['ey']}px;transform:rotate(6deg);filter:drop-shadow(0 10px 18px rgba(80,60,150,.18))}}
.st1{{left:{P['s1x']}px;top:{P['s1y']}px}}
.st2{{left:{P['s2x']}px;top:{P['s2y']}px;transform:rotate(16deg)}}
</style></head><body>
<div class="blob"></div>
<img class="st st2" src="zvezdy-v.png">
<img class="logo" src="logo-conf.png"><div class="ln"></div>
<div class="h">Ответ на требования <span class="pill">ФНС.</span><span class="q">Как не навредить себе?</span></div>
<div class="card"><img src="trebus-cutout.png"></div>
<img class="env" src="envelope.svg">
</body></html>"""
sq=dict(m=70,ly=50,lw=170,hy=190,hs=74,bx=130,by=540,bd=1000,b2x=-70,b2y=900,b2d=170,
        cx=170,cy=610,cw=740,ch=380,tw=300,sw=110,ew=170,ex=790,ey=520,s1x=925,s1y=660,s2x=55,s2y=760)
st=dict(m=90,ly=110,lw=240,hy=390,hs=98,bx=-60,by=1040,bd=1300,b2x=-80,b2y=1740,b2d=220,
        cx=130,cy=1190,cw=820,ch=480,tw=380,sw=150,ew=200,ex=770,ey=1110,s1x=850,s1y=1730,s2x=50,s2y=1050)
open("partner-square.html","w").write(page(1080,1080,sq))
open("partner-story.html","w").write(page(1080,1920,st))
