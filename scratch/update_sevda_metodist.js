const fs = require('fs');
const path = require('path');

const rootDir = '/Users/konul/Documents/esas2 copy 2';
const scriptJsPath = path.join(rootDir, 'script.js');
const backupJsPath = path.join(rootDir, 'scratch/script_working_backup.js');

let js = fs.readFileSync(scriptJsPath, 'utf8');

// 1. Update staffData.departments and commissions
const targetBlock = `    {
      id: "26",
      name_az: "Şəlalə Zeynalova Qara qızı",
      name_en: "Shalala Zeynalova Gara",
      name_ru: "Шалаля Зейналова Гара гызы",
      role_az: "Metodist",
      role_en: "Methodist",
      role_ru: "Методист",
      img: "selalex1.jpeg",
    },
  ],
  commissions: [
    {
      id: "25",
      name_az: "Sevda Bağızadə Əmrulla qızı",
      name_en: "Sevda Bagizada Amrulla",
      name_ru: "Севда Багизаде Амрулла гызы",
      role_az: '"Telekommunikasiya" fənn birləşmə komissiyası',
      role_en: '"Telecommunications" Subject Commission',
      role_ru: 'Предметная комиссия "Телекоммуникации"',
      img: "sevda.jpeg",
    },
  ],`;

const replacementBlock = `    {
      id: "25",
      name_az: "Sevda Bağızadə Əmrulla qızı",
      name_en: "Sevda Bagizada Amrulla",
      name_ru: "Севда Багизаде Амрулла гызы",
      role_az: "Metodist",
      role_en: "Methodist",
      role_ru: "Методист",
      img: "sevda.jpeg",
    },
    {
      id: "26",
      name_az: "Şəlalə Zeynalova Qara qızı",
      name_en: "Shalala Zeynalova Gara",
      name_ru: "Шалаля Зейналова Гара гызы",
      role_az: "Metodist",
      role_en: "Methodist",
      role_ru: "Методист",
      img: "selalex1.jpeg",
    },
  ],
  commissions: [
    {
      id: "25",
      name_az: "Sevda Bağızadə Əmrulla qızı",
      name_en: "Sevda Bagizada Amrulla",
      name_ru: "Севда Багизаде Амрулла гызы",
      role_az: "Metodist",
      role_en: "Methodist",
      role_ru: "Методист",
      img: "sevda.jpeg",
    },
  ],`;

if (js.includes(targetBlock)) {
  js = js.replace(targetBlock, replacementBlock);
} else {
  console.log('Target block not found, check formatting');
}

// 2. Update wingAdminStaff definition so it cleanly uses staffData.departments
const targetWing = `    const wingAdminStaff = [
      ...staffData.departments.filter((p) =>
        ["13", "19", "16", "20", "22", "18", "26"].includes(p.id)
      ),
      ...staffData.commissions.filter((p) => p.id === "25"),
    ];`;

const replacementWing = `    const wingAdminStaff = staffData.departments.filter((p) =>
      ["13", "19", "16", "20", "22", "18", "25", "26"].includes(p.id)
    );`;

if (js.includes(targetWing)) {
  js = js.replace(targetWing, replacementWing);
}

fs.writeFileSync(scriptJsPath, js, 'utf8');
fs.writeFileSync(backupJsPath, js, 'utf8');
console.log('Updated Sevda to Metodist in script.js and backup!');

