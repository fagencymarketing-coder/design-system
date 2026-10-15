// PNG-версии иконок и знаков для замены в PPTX: сплошные и готовые «водяные» (с прозрачностью)
const {chromium}=require('playwright'); const fs=require('fs'), path=require('path');
const root=path.resolve(__dirname,'../..');
const VARS=[['crimson','#D73A61',1],['graphite','#1C1A17',1],['white','#FFFFFF',1],['vodyanoy-svetlyj','#ABAD58',0.24],['vodyanoy-temnyj','#D2BE8C',0.16],['vodyanoy-zelenyj','#FFFFFF',0.14]];
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--allow-file-access-from-files']});
  const out=path.join(root,'editable','icons-png'); fs.mkdirSync(out,{recursive:true});
  const tmp=path.join(__dirname,'out','_i.html');
  for(const dir of ['assets/icons','assets/marks']){
    for(const f of fs.readdirSync(path.join(root,dir)).filter(x=>x.endsWith('.svg'))){
      for(const [vn,col,op] of VARS){
        fs.writeFileSync(tmp,'<html><body style="margin:0;background:transparent"><div style="width:700px;height:700px;background:'+col+';opacity:'+op+';-webkit-mask:url(file://'+path.join(root,dir,f)+') center/contain no-repeat;mask:url(file://'+path.join(root,dir,f)+') center/contain no-repeat"></div></body></html>');
        const p=await b.newPage({viewport:{width:700,height:700}}); await p.goto('file://'+tmp); await p.waitForTimeout(150);
        await p.screenshot({path:path.join(out,f.replace('.svg','')+'-'+vn+'.png'),omitBackground:true}); await p.close();
      }
    }
  }
  await b.close(); console.log('icons done');
})();
