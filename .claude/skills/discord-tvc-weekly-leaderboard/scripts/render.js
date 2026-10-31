// Usage: node render.js <leaderboard.html> <data.json> <out.png>
// data.json: {"dates":"Oct 18 – 24, 2026","top":[{"h":"handle","g":515.19,"a":null}, ... 5 rows]}
// "a" is an optional photo file next to the HTML; null shows the empty profile picture.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [html,data,out]=process.argv.slice(2);
 const d=encodeURIComponent(fs.readFileSync(data,'utf8'));
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+path.resolve(html)+'?d='+d,{waitUntil:'networkidle',timeout:20000}).catch(()=>{});
 await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
 await p.locator('.card').screenshot({path:out});console.log('rendered',out);await b.close()})();
