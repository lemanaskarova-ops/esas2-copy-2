const fs = require('fs');

function moveSevda(filePath) {
  let code = fs.readFileSync(filePath, 'utf8');

  // Update wings definition in renderTree()
  const oldWings = `    // 4-cü Səviyyə: Şöbə Müdirləri & Birləşmə Komissiyaları (2 Balanslaşdırılmış Qanad)
    const wingAcademicStaff = [
      ...staffData.departments.filter((p) => ["7", "9", "23", "14", "24", "11"].includes(p.id)),
      ...staffData.commissions.filter((p) => p.id === "25"),
    ];
    const wingAdminStaff = staffData.departments.filter((p) =>
      ["13", "19", "16", "20", "22", "18", "26"].includes(p.id)
    );`;

  const newWings = `    // 4-cü Səviyyə: Şöbə Müdirləri & Birləşmə Komissiyaları (2 Balanslaşdırılmış Qanad)
    const wingAcademicStaff = staffData.departments.filter((p) =>
      ["7", "9", "23", "14", "24", "11", "26"].includes(p.id)
    );
    const wingAdminStaff = [
      ...staffData.departments.filter((p) =>
        ["13", "19", "16", "20", "22", "18"].includes(p.id)
      ),
      ...staffData.commissions.filter((p) => p.id === "25"),
    ];`;

  if (code.includes(oldWings)) {
    code = code.replace(oldWings, newWings);
    console.log("Successfully updated wings in", filePath);
  } else {
    console.log("oldWings block not found exactly in", filePath);
  }

  fs.writeFileSync(filePath, code, 'utf8');
}

moveSevda('/Users/konul/Documents/esas2 copy 2/scratch/script_working_backup.js');
moveSevda('/Users/konul/Documents/esas2 copy 2/script.js');
console.log("Done moving Sevda to Admin wing!");

