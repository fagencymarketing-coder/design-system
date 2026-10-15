// Проверка шаблонов: загрузка, fit.js, предупреждения. Использование: node tools/check-templates.js
const {chromium}=require('playwright'); const fs=require('fs'), path=require('path');
const dir=path.resolve(__dirname,'../templates');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--allow-file-access-from-files']});
  for(const f of fs.readdirSync(dir).filter(x=>/^[VU]\d+.*\.html$/.test(x)).sort()){
    const p=await b.newPage({viewport:{width:1080,height:1080}});
    await p.goto('file://'+path.join(dir,f)); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
    const r=await p.evaluate(()=>({fit:document.body.dataset.fitStatus,rep:window.__fitReport,sizes:[...document.querySelectorAll('[data-fit]')].map(e=>e.dataset.slot+':'+e.dataset.fontSize)}));
    console.log(f.padEnd(34),r.fit,r.sizes.join(' '),r.rep&&r.rep.length?'!! '+r.rep.join(' | '):'');
    await p.close();
  }
  await b.close();
})();
