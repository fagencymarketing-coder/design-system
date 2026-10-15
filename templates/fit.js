/* Автоподбор кегля по лестнице размеров + проверка раскладки. Подключается внизу каждого шаблона.
   Элемент с data-fit: data-sizes="146,104,80,62" (от большего к меньшему), data-max-width (px, по умолчанию 888),
   data-max-lines (по умолчанию 4). Строки делятся вручную через <br>. Результат: document.body.dataset.fitStatus = "ok" | "warn",
   список замечаний в window.__fitReport; при ?debug замечания показываются на макете. */
(function(){
  var report=[];
  function wOf(el){var r=document.createRange();r.selectNodeContents(el);return r.getBoundingClientRect().width;}
  document.querySelectorAll('[data-fit]').forEach(function(el){
    var sizes=(el.dataset.sizes||'').split(',').map(Number).filter(Boolean);
    var maxW=parseFloat(el.dataset.maxWidth||888), maxL=parseInt(el.dataset.maxLines||4,10);
    var lines=el.querySelectorAll('br').length+1, ok=false, used=null;
    if(lines>maxL) report.push((el.dataset.slot||'text')+': строк '+lines+' > '+maxL);
    for(var i=0;i<sizes.length;i++){ el.style.fontSize=sizes[i]+'px'; if(wOf(el)<=maxW){ok=true;used=sizes[i];break;} }
    if(!ok){ report.push((el.dataset.slot||'text')+': не помещается даже при '+sizes[sizes.length-1]+' px, сократите текст или смените шаблон'); }
    el.dataset.fontSize=used||sizes[sizes.length-1];
  });
  var logo=document.querySelector('.logo'), blk=document.querySelector('.text-top,.text-mid');
  if(logo&&blk){var a=logo.getBoundingClientRect(),b=blk.getBoundingClientRect();
    if(b.top<a.bottom+24) report.push('блок текста ближе 24 px к логотипу'); if(b.bottom>1080-96) report.push('блок текста ниже поля 96 px');}
  document.body.dataset.fitStatus=report.length?'warn':'ok'; window.__fitReport=report;
  if(report.length) console.warn('[fit]',report.join(' | '));
  if(/debug/.test(location.search)&&report.length){var d=document.createElement('div');
    d.style.cssText='position:absolute;left:12px;top:12px;right:12px;background:#d00;color:#fff;font:14px/1.3 sans-serif;padding:8px 12px;z-index:99';
    d.textContent=report.join(' | ');document.body.appendChild(d);}
})();
