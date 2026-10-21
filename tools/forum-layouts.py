# Генератор макетов форума (квадрат и сториз): python3 tools/forum-layouts.py из папки examples/
T=['Налоги','Дробление','ИФНС','ИИ','Закрытие года']
li=''.join(f'<li><b>PRO</b>{t}</li>' for t in T)
GIRL='<img class="girl" src="../assets/event/girl-abacus.png" alt="">'
ADDR='ул.&nbsp;Пушкина, д.&nbsp;41 · Театр кукол «Сказка»'
DATE='5&nbsp;ноября 2026&nbsp;г.<span class="city">Барнаул</span>'
PAGE='''<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>@TITLE@</title>
<link rel="stylesheet" href="../templates/base.css"><style>
html,body{height:@H@px}.canvas{height:@H@px;background:var(--paper);color:#1C1A17}
.logo{top:@LOGO@px;width:200px}
.stack{position:absolute;left:96px;top:@ST@px;bottom:@SB@px;display:flex;flex-direction:column;justify-content:space-between;z-index:3}
.head .dash2{width:64px;height:4px;background:#D6001F;margin-bottom:22px}
.eyebrow{font-weight:600;font-size:26px;letter-spacing:.16em;text-transform:uppercase;color:#6A6965;white-space:nowrap}
.t{font-weight:700;line-height:.98;letter-spacing:-.035em;white-space:nowrap;font-size:@TS@px}
.wm{width:690px;height:92px;-webkit-mask:url(../assets/event/wordmark-skazochnaya-buhgalteriya.png) left center/contain no-repeat;mask:url(../assets/event/wordmark-skazochnaya-buhgalteriya.png) left center/contain no-repeat;background:#7160A3}
.topics{list-style:none}
.topics li{display:flex;align-items:center;font-weight:600;font-size:@PS@px;line-height:1;letter-spacing:-.01em;height:@PH@px;margin-bottom:@PM@px}
.topics li:last-child{margin-bottom:0}
.topics b{display:inline-block;text-align:center;font-weight:800;letter-spacing:.12em;padding-left:.12em;width:@PW@px;height:@PH@px;line-height:@PH@px;margin-right:@PG@px;font-size:@PF@px;color:#D6001F}
.plates .topics b{background:#D6001F;color:#fff;border-radius:9px}
.date{font-weight:700;font-size:@DS@px;letter-spacing:-.02em;white-space:nowrap;margin-bottom:@DM@px}
.city{margin-left:@CG@px;letter-spacing:.06em;text-transform:uppercase;color:#7160A3}
.addr{font-weight:500;font-size:@AS@px;color:#6A6965;white-space:nowrap}
.girl{position:absolute;display:block}
@CSS@
</style></head><body><div class="canvas @CLS@">
<img class="logo" src="../assets/event/logo-forum.png" alt="">
@BODY@
</div></body></html>'''
SQ=dict(H=1080,LOGO=96,ST=236,SB=96,TS=88,PS=56,PH=56,PM=10,PW=130,PG=26,PF=31,DS=48,DM=14,CG=24,AS=26)
STO=dict(H=1920,LOGO=240,ST=424,SB=420,TS=124,PS=64,PH=62,PM=16,PW=150,PG=30,PF=34,DS=62,DM=20,CG=28,AS=30)
def build(name,fmt,cls,css,body):
    s=PAGE
    for k,v in fmt.items(): s=s.replace('@'+k+'@',str(v))
    s=s.replace('@TITLE@',name).replace('@CSS@',css).replace('@CLS@',cls).replace('@BODY@',body)
    open(name+'.html','w').write(s)
HEAD='<div class="head"><div class="dash2"></div><div class="eyebrow">III форум главных бухгалтеров</div></div>'
TITLE='<div class="t">Сказочная<br>бухгалтерия</div>'
def stack(inner): return '<div class="stack">'+inner+'</div>'
BOT=f'<div><div class="date">{DATE}</div><div class="addr">{ADDR}</div></div>'
def std(name,fmt,cls,css,girlcss):
    body=stack(HEAD+TITLE+f'<ul class="topics">{li}</ul>'+BOT)+GIRL
    build(name,fmt,cls,css+girlcss,body)
# F / E / B — квадрат и сториз
for fmt,pre in ((SQ,'forum'),(STO,'story')):
    sto=pre=='story'
    std(f'{pre}-f',fmt,'plates','',('.girl{right:36px;top:1500px;height:620px}' if sto else '.girl{right:36px;top:880px;height:620px}'))
    std(f'{pre}-e',fmt,'plates','',('.girl{right:-6px;top:1440px;height:900px}' if sto else '.girl{right:-10px;top:790px;height:780px}'))
    std(f'{pre}-b',fmt,'',('.stack{}' ),('.girl{right:60px;top:770px;height:520px}' if sto else '.girl{right:30px;top:420px;height:660px}'))
# I — светлый верх + панель
def pan(name,fmt,ptop,wmtop,girlcss,pad,plates=True,pill=False):
    sto=fmt is STO
    top=f'<div class="stack top" style="bottom:auto;top:{fmt["ST"]}px">{HEAD}<div class="wm" style="margin-top:{wmtop}px"></div></div>'
    panel=f'<div class="panel" style="top:{ptop}px"><div class="pstack" style="top:{pad}px;bottom:{fmt["SB"]}px"><ul class="topics">{li}</ul>{BOT}</div></div>'
    PILL='.panel .topics li{background:#F3EEDC;color:#1C1A17;border-radius:999px;padding:0 34px 0 30px;width:fit-content;margin-bottom:26px}.panel .topics li:last-child{margin-bottom:0}.panel .topics b{color:#D6001F;width:auto;padding-left:0;margin-right:22px}'
    PLATE='.panel .topics li{color:#F3EEDC}.panel .topics b{background:#D6001F;color:#fff;border-radius:9px}'
    PLAIN='.panel .topics li{color:#F3EEDC}.panel .topics b{color:#D6001F;background:none;width:112px;padding-left:0;text-align:left}'
    css=('.panel{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(165deg,#7160A3 0%,#7E7BC4 65%,#8899EB 100%);z-index:2}'
      '.pstack{position:absolute;left:96px;display:flex;flex-direction:column;justify-content:space-between}'
      +(PILL if pill else PLATE if plates else PLAIN)+
      '.panel .date,.panel .city{color:#F3EEDC}.panel .addr{color:rgba(243,238,220,.9)}'+girlcss)
    build(name,fmt,'',css,top+GIRL+panel)
pan('forum-i',SQ,458,40,'.girl{right:24px;top:240px;height:560px;z-index:1}',34)
pan('story-i',dict(STO,SB=340),760,60,'.girl{right:24px;top:500px;height:640px;z-index:1}',64,False)

pan('story-i-pill',dict(STO,SB=340),760,60,'.girl{right:24px;top:500px;height:640px;z-index:1}',64,False,True)
