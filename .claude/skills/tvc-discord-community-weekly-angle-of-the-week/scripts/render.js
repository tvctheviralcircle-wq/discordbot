// Usage: node render.js <card.html> <out.png>
// Renders the .card element at 2x. Run from any directory; Playwright's Chromium is preinstalled.
const {chromium}=require('playwright');
(async()=>{
  const [html,out]=process.argv.slice(2);
  if(!html||!out){console.error('usage: node render.js <card.html> <out.png>');process.exit(1);}
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1200,height:800},deviceScaleFactor:2});
  await p.goto('file://'+require('path').resolve(html),{waitUntil:'networkidle',timeout:20000}).catch(()=>{});
  await p.evaluate(()=>document.fonts.ready);
  await p.waitForTimeout(1500);
  await p.locator('.card').screenshot({path:out});
  const box=await p.locator('.card').boundingBox();
  console.log(`rendered ${out} (${Math.round(box.width)}x${Math.round(box.height)} css px)`);
  await b.close();
})();
