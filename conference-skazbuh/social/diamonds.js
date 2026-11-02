function strip(y,w,size,gap){var c=['#d6001f','#ffffff','#8f9be8','#e0476f','#d6001f','#b9aee0'];var n=Math.ceil(w/(size+gap))+2;
 for(var i=0;i<n;i++){var d=document.createElement('div');d.className='dm';d.style.width=d.style.height=size+'px';d.style.left=(i*(size+gap)-size/2)+'px';d.style.top=y+'px';d.style.background=c[i%c.length];document.body.appendChild(d);}}
