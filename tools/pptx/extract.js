// Извлекает из HTML-макета: фон (PNG без текста, логотипов, картинок и черт), тексты по строкам, картинки, черты.
const {chromium}=require('playwright');
const fs=require('fs'), path=require('path');
const root=path.resolve(__dirname,'../..');
const LAYOUTS=JSON.parse(fs.readFileSync(path.join(__dirname,'layouts.json'),'utf8'));
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--allow-file-access-from-files']});
  const out={};
  fs.mkdirSync(path.join(__dirname,'out'),{recursive:true});
  for(const L of LAYOUTS){
    const p=await b.newPage({viewport:{width:1080,height:1080}});
    await p.goto('file://'+path.join(root,L.html));
    await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
    const data=await p.evaluate((keep)=>{
      const res={imgs:[],dashes:[],texts:[]};
      const isKept=el=>keep.some(s=>el.closest(s));
      document.querySelectorAll('img').forEach(im=>{const r=im.getBoundingClientRect();res.imgs.push({src:im.src,x:r.left,y:r.top,w:r.width,h:r.height,logo:/logo/.test(im.src)});});
      document.querySelectorAll('.dash').forEach(el=>{const r=el.getBoundingClientRect();res.dashes.push({x:r.left,y:r.top,w:r.width,h:r.height,color:getComputedStyle(el).backgroundColor});});
      const nonInline=el=>{while(el&&getComputedStyle(el).display.startsWith('inline'))el=el.parentElement;return el;};
      const groups=new Map();
      const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
      let n; while(n=walker.nextNode()){
        if(!n.textContent.trim())continue;
        const pe=n.parentElement; if(pe.closest('script,style')||isKept(pe))continue;
        const root=nonInline(pe); if(!groups.has(root))groups.set(root,[]); groups.get(root).push(n);
      }
      for(const [root,nodes] of groups){
        const lines=[]; let fs0=null,lh=null,tt='none';
        for(const node of nodes){
          const cs=getComputedStyle(node.parentElement);
          const st={color:cs.color,weight:parseInt(cs.fontWeight),size:parseFloat(cs.fontSize),ls:cs.letterSpacing==='normal'?0:parseFloat(cs.letterSpacing),tt:cs.textTransform};
          if(fs0===null){fs0=st.size;lh=cs.lineHeight==='normal'?st.size*1.2:parseFloat(cs.lineHeight);}
          if(st.tt!=='none')tt=st.tt;
          const t=node.textContent;
          for(let i=0;i<t.length;i++){
            const rg=document.createRange(); rg.setStart(node,i); rg.setEnd(node,i+1);
            const rs=rg.getClientRects(); if(!rs.length)continue; const r=rs[0];
            if(r.width===0&&t[i]!==' '&&t[i]!==' ')continue;
            let ln=lines[lines.length-1];
            if(!ln||r.top>ln.top+st.size*0.5){ln={top:r.top,bottom:r.bottom,left:r.left,right:r.right,runs:[]};lines.push(ln);}
            ln.right=Math.max(ln.right,r.right); ln.bottom=Math.max(ln.bottom,r.bottom);
            const last=ln.runs[ln.runs.length-1];
            if(last&&JSON.stringify(last.st)===JSON.stringify(st))last.text+=t[i]; else ln.runs.push({text:t[i],st});
          }
        }
        if(!lines.length)continue;
        // trailing spaces
        lines.forEach(l=>{const lr=l.runs[l.runs.length-1]; lr.text=lr.text.replace(/\s+$/,'');});
        const rr=root.getBoundingClientRect();
        res.texts.push({lines:lines.map(l=>({top:l.top,bottom:l.bottom,left:l.left,right:l.right,runs:l.runs})),size:fs0,lh,tt,cls:root.className,tag:root.tagName});
      }
      // псевдоэлементы ::before с текстом (маркеры списка)
      document.querySelectorAll('li').forEach(li=>{
        const ps=getComputedStyle(li,'::before'); const c=ps.content;
        if(c&&c!=='none'&&c!=='normal'){const r=li.getBoundingClientRect();
          res.texts.push({marker:true,text:c.replace(/^["']|["']$/g,''),x:r.left,y:r.top,color:ps.color,size:parseFloat(ps.fontSize),weight:parseInt(ps.fontWeight),lh:parseFloat(li.style.lineHeight)||parseFloat(getComputedStyle(li).lineHeight)});}
      });
      return res;
    },L.keep||[]);
    // фон: прячем текст, логотипы, картинки, черты
    const sel=(L.keep||[]).map(k=>':not('+k+'):not('+k+' *)').join('');
    await p.addStyleTag({content:'*'+sel+'{color:transparent!important;-webkit-text-stroke:0!important;text-shadow:none!important} img,.dash{visibility:hidden!important} li::before{color:transparent!important}'});
    await p.screenshot({path:path.join(__dirname,'out',L.name+'-bg.png')});
    out[L.name]=data;
    await p.close();
  }
  fs.writeFileSync(path.join(__dirname,'out','layouts-data.json'),JSON.stringify(out,null,1));
  await b.close(); console.log('extracted',Object.keys(out).length);
})();
