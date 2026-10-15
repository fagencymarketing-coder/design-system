// Рендерит шаблоны в PNG 1080×1080 (templates/previews). Использование: node tools/render-templates.js
const {chromium}=require('playwright'); const fs=require('fs'), path=require('path');
const dir=path.resolve(__dirname,'../templates'), out=path.join(dir,'previews'); fs.mkdirSync(out,{recursive:true});
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--allow-file-access-from-files']});
  for(const f of fs.readdirSync(dir).filter(x=>/^[VU]\d+.*\.html$/.test(x)).sort()){
    const p=await b.newPage({viewport:{width:1080,height:1080}});
    await p.goto('file://'+path.join(dir,f)); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
    await p.screenshot({path:path.join(out,f.replace('.html','.png'))}); await p.close();
  }
  await b.close(); console.log('previews done');
})();
