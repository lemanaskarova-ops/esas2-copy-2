const fs = require('fs');
const path = require('path');

const rootDir = '/Users/konul/Documents/esas2 copy 2';
const scriptJsPath = path.join(rootDir, 'script.js');
const backupJsPath = path.join(rootDir, 'scratch/script_working_backup.js');

let js = fs.readFileSync(scriptJsPath, 'utf8');

// 1. Update wingAcademicStaff in renderStructureTree
const targetWing = `    const wingAcademicStaff = staffData.departments.filter((p) =>
      ["7", "9", "23", "14", "24", "11"].includes(p.id)
    );`;

const replacementWing = `    const academicOrder = ["7", "23", "24", "9", "14", "11"];
    const wingAcademicStaff = academicOrder
      .map((id) => staffData.departments.find((p) => p.id === id))
      .filter(Boolean);`;

if (js.includes(targetWing)) {
  js = js.replace(targetWing, replacementWing);
} else {
  console.log('targetWing not found, checking alternatives...');
}

fs.writeFileSync(scriptJsPath, js, 'utf8');
fs.writeFileSync(backupJsPath, js, 'utf8');
console.log('Reordered academic staff in script.js and backup!');

