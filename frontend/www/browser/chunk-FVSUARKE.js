import{c}from"./chunk-G3CV3VGG.js";import{a as l}from"./chunk-6O5TN2LV.js";import{f as s}from"./chunk-PG5KTQWO.js";var C="ION-CONTENT",i="ion-content",a=".ion-content-scroll-host",T=`${i}, ${a}`,n=o=>o.tagName===C,m=o=>s(void 0,null,function*(){return n(o)?(yield new Promise(t=>l(o,t)),o.getScrollElement()):o}),E=o=>{let t=o.querySelector(a);return t||o.querySelector(T)},O=o=>o.closest(T),p=(o,t)=>n(o)?o.scrollToTop(t):Promise.resolve(o.scrollTo({top:0,left:0,behavior:t>0?"smooth":"auto"})),S=(o,t,r,e)=>n(o)?o.scrollByPoint(t,r,e):Promise.resolve(o.scrollBy({top:r,left:t,behavior:e>0?"smooth":"auto"})),_=o=>c(o,i),y=o=>{if(n(o)){let t=o,r=t.scrollY;return t.scrollY=!1,r}else return o.style.setProperty("overflow","hidden"),!0},I=(o,t)=>{n(o)?o.scrollY=t:o.style.removeProperty("overflow")};export{n as a,m as b,E as c,O as d,p as e,S as f,_ as g,y as h,I as i};
