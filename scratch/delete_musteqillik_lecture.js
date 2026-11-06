const fs = require('fs');
const path = require('path');

const rootDir = '/Users/konul/Documents/esas2 copy 2';
const indexHtmlPath = path.join(rootDir, 'index.html');
const scriptJsPath = path.join(rootDir, 'script.js');
const backupJsPath = path.join(rootDir, 'scratch/script_working_backup.js');

// 1. UPDATE script.js
let js = fs.readFileSync(scriptJsPath, 'utf8');

const targetLecture = `  {
    id: 17,
    title_az: "Azərbaycan tarixi: Müstəqillik yolu və intibah",
    title_en: "History of Azerbaijan: Path to Independence",
    title_ru: "История Азербайджана: Путь к независимости",
    duration: "22:00",
    thumb: "https://img.youtube.com/vi/UZrba576_T8/hqdefault.jpg",
    category: "tarix",
    url: "https://www.youtube.com/watch?v=UZrba576_T8",
  },
`;

if (js.includes(targetLecture)) {
  js = js.replace(targetLecture, '');
  console.log('Removed lecture id 17 from script.js');
} else {
  console.log('Target lecture not found in script.js');
}

// Update counts in getUIText
js = js.replace('deptAllMeta: "35 Video Lessons · 8 Departments"', 'deptAllMeta: "34 Video Lessons · 8 Departments"');
js = js.replace('deptHistMeta: "8 Video Lessons · History & Victory"', 'deptHistMeta: "7 Video Lessons · History & Victory"');

js = js.replace('deptAllMeta: "35 видеоуроков · 8 предметов"', 'deptAllMeta: "34 видеоурока · 8 предметов"');
js = js.replace('deptHistMeta: "8 видеоуроков · История Азербайджана"', 'deptHistMeta: "7 видеоуроков · История Азербайджана"');

js = js.replace('deptAllMeta: "35 Videodərs · 8 Fənn Bölməsi"', 'deptAllMeta: "34 Videodərs · 8 Fənn Bölməsi"');
js = js.replace('deptHistMeta: "8 Videodərs · Tarix və Zəfər"', 'deptHistMeta: "7 Videodərs · Tarix və Zəfər"');

fs.writeFileSync(scriptJsPath, js, 'utf8');
fs.writeFileSync(backupJsPath, js, 'utf8');
console.log('script.js and script_working_backup.js updated!');

// 2. UPDATE index.html
let html = fs.readFileSync(indexHtmlPath, 'utf8');

// Update badges and meta
html = html.replace('35 Videodərs · Bütün fənlər', '34 Videodərs · Bütün fənlər');
html = html.replace('8 Videodərs · Tarix və Zəfər', '7 Videodərs · Tarix və Zəfər');
html = html.replace('<span class="lecture-dept-badge" id="dept-count-all">35</span>', '<span class="lecture-dept-badge" id="dept-count-all">34</span>');
html = html.replace('<span class="lecture-dept-badge" id="dept-count-tarix">8</span>', '<span class="lecture-dept-badge" id="dept-count-tarix">7</span>');
html = html.replace('Hamısı (35)', 'Hamısı (34)');
html = html.replace('Azərbaycan Tarixi (8)', 'Azərbaycan Tarixi (7)');
html = html.replace('8 videodərs · Tarix və Zəfər', '7 videodərs · Tarix və Zəfər');

// Bump cache version to v=20261105_12
html = html.replace(/20261105_11/g, '20261105_12');

fs.writeFileSync(indexHtmlPath, html, 'utf8');
console.log('index.html updated with new counts and cache version!');

