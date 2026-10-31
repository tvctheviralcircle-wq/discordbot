// Usage: node render.js <milestone-card.html> <stage> <handle> <out.png> [avatar.jpg]
// stage: 1 | 3 | 10 | 30 | 50. Put logo.png (and the avatar, if any) next to the HTML.
// Leave the avatar out to get the empty profile picture.
const {chromium}=require('playwright');const path=require('path');
(async()=>{
  const [html,stage,handle,out,avatar]=process.argv.slice(2);
  if(!html||!stage||!handle||!out){console.error('usage: node render.js <card.html> <stage> <handle> <out.png> [avatar]');process.exit(1);}
  const q=new URLSearchParams({stage,handle});if(avatar)q.set('avatar',avatar);
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});
  await p.goto('file://'+path.resolve(html)+'?'+q,{waitUntil:'networkidle',timeout:20000}).catch(()=>{});
  await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
  await p.locator('.card').screenshot({path:out});console.log('rendered',out);await b.close();
})();
