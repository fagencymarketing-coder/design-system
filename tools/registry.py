#!/usr/bin/env python3
"""Журнал макетов: что делали, что утверждено, что нельзя повторять.
  registry.py report                         пересобрать registry/LOG.md
  registry.py add "Тема" V2 графит --photo X --accent слово --mark Y [--note ...] [--file ...]
  registry.py status <id> утверждён|отклонён|опубликован|снят [--note ...]
  registry.py suggest [--last 8]            что недавно использовано: фото, шаблоны, регистры (чего избегать)
  registry.py unused                        фото из библиотеки assets/team, которых ещё нет в журнале (брать только их)"""
import json, sys, os, datetime, collections, argparse
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','registry')
J=os.path.join(P,'layouts.json')
def load(): return json.load(open(J,encoding='utf8'))
def save(e): json.dump(e,open(J,'w',encoding='utf8'),ensure_ascii=False,indent=1); report(e)
def report(e=None):
    e=e or load(); L=['# Журнал макетов','','Статусы: **утверждён** (можно брать за образец), **предложен** (ждёт решения), **отклонён** (не повторять),',
      '**опубликован**, **снят** (шаблон убран из набора). Обновляется командой `tools/registry.py` или вручную в `layouts.json`.','',
      '| id | дата | тема | шаблон | регистр | фото | акцент | знак | статус | заметка |','|---|---|---|---|---|---|---|---|---|---|']
    for x in e: L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |'%(x['id'],x['date'],x['topic'],x['template'],x['register'],x['photo'] or '—',x['accent'] or '—',x['watermark'] or '—',x['status'],x['note'] or ''))
    open(os.path.join(P,'LOG.md'),'w',encoding='utf8').write('\n'.join(L)+'\n')
def suggest(n):
    e=[x for x in load() if x['status']!='снят'][-n:]
    ph=collections.Counter(x['photo'] for x in e if x['photo']); rg=collections.Counter(x['register'] for x in e); tp=collections.Counter(x['template'] for x in e)
    print('Последние %d макетов.'%len(e))
    print('Фото (не повторять, если можно): ',', '.join('%s×%d'%kv for kv in ph.most_common()) or '—')
    print('Регистры: ',', '.join('%s×%d'%kv for kv in rg.most_common()))
    print('Шаблоны: ',', '.join('%s×%d'%kv for kv in tp.most_common()))
    rej=[x for x in load() if x['status']=='отклонён']
    if rej: print('Отклонено ранее: ',', '.join('%s %s (%s)'%(x['template'],x['register'],x['note']) for x in rej[-5:]))
    top=rg.most_common(1)[0]
    if top[1]>=3: print('! Регистр «%s» уже %d раза в последних %d: предложить другой (светлый/фото/зелёный).'%(top[0],top[1],len(e)))
if __name__=='__main__':
    a=sys.argv[1:]; cmd=a[0] if a else 'report'
    if cmd=='report': report(); print('LOG.md обновлён')
    elif cmd=='unused':
        import re,glob
        used={m.group(1)+'-'+m.group(2) for x in load() for m in [re.search(r'(concrete|plaster|studio|color|office)-(\d+)',x['photo'] or '')] if m}
        root=os.path.join(P,'..','assets','team')
        free=sorted(os.path.basename(f)[:-4] for f in glob.glob(os.path.join(root,'*.jpg')))
        print('Использованы за всё время:',', '.join(sorted(used)))
        print('Свободны:',', '.join(f for f in free if f not in used))
        print('Внимание: кадры одной сцены (concrete-0244/0253, 0259/0265/0267/0269, 0283/0289, 0297/0302) выглядят как повтор, берите другую сцену.')
    elif cmd=='suggest':
        ap=argparse.ArgumentParser(); ap.add_argument('--last',type=int,default=8); suggest(ap.parse_args(a[1:]).last)
    elif cmd=='add':
        ap=argparse.ArgumentParser(); ap.add_argument('topic'); ap.add_argument('template'); ap.add_argument('register')
        ap.add_argument('--photo',default=''); ap.add_argument('--accent',default=''); ap.add_argument('--mark',default=''); ap.add_argument('--note',default=''); ap.add_argument('--file',default='')
        o=ap.parse_args(a[1:]); e=load(); d=datetime.date.today().isoformat()
        e.append(dict(id='%s-%02d'%(d,len([x for x in e if x['date']==d])+1),date=d,topic=o.topic,template=o.template,register=o.register,photo=o.photo,accent=o.accent,watermark=o.mark,status='предложен',note=o.note,file=o.file))
        save(e); print('добавлено',e[-1]['id'])
    elif cmd=='status':
        ap=argparse.ArgumentParser(); ap.add_argument('id'); ap.add_argument('status'); ap.add_argument('--note',default=''); o=ap.parse_args(a[1:]); e=load()
        for x in e:
            if x['id']==o.id: x['status']=o.status; x['note']=o.note or x['note']
        save(e); print('ок')
