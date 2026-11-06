const fs = require('fs');

const targetFile = '/Users/konul/Documents/esas2 copy 2/scratch/script_working_backup.js';
let code = fs.readFileSync(targetFile, 'utf8');

// 1. Replace avatar_natiq.svg with natiqx2.jpeg
code = code.replace(/id:\s*"24"[\s\S]*?img:\s*"[^"]+"/, (m) => m.replace(/img:\s*"[^"]+"/, 'img: "natiqx2.jpeg"'));

// 2. Replace resmiyyeson.png with resmiyyex.jpeg
code = code.replace(/id:\s*"14"[\s\S]*?img:\s*"[^"]+"/, (m) => m.replace(/img:\s*"[^"]+"/, 'img: "resmiyyex.jpeg"'));

// 3. Replace gunayson.png with gunayx.jpeg
code = code.replace(/id:\s*"18"[\s\S]*?img:\s*"[^"]+"/, (m) => m.replace(/img:\s*"[^"]+"/, 'img: "gunayx.jpeg"'));

// 4. Replace lemanson.jpg with lemanx1.jpeg
code = code.replace(/id:\s*"20"[\s\S]*?img:\s*"[^"]+"/, (m) => m.replace(/img:\s*"[^"]+"/, 'img: "lemanx1.jpeg"'));

// 5. Add Shalala Zeynalova if not present
if (!code.includes('Şəlalə Zeynalova')) {
  const xelilTarget = 'img: "xelilson.jpeg",\n    },';
  const selaleEntry = `img: "xelilson.jpeg",
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
    },`;
  code = code.replace(xelilTarget, selaleEntry);
}

// 6. Update photoClass in openPersonDetail
const oldPhotoClassBlock = `    let photoClass = "";
    if (person.id === "2") photoClass = "sahmurad-photo";
    else if (person.id === "7") photoClass = "babek-photo";
    else if (person.id === "12") photoClass = "seide-photo";
    else if (person.id === "16") photoClass = "vefa-photo";
    else if (person.id === "18") photoClass = "gunay-photo";
    else if (person.id === "23") photoClass = "yegane-photo";
    else if (person.id === "25") photoClass = "sevda-photo";
    else if (person.id === "13" || (person.img && person.img.includes("fizuli"))) photoClass = "fizuli-photo";`;

const newPhotoClassBlock = `    let photoClass = "";
    if (person.id === "1") photoClass = "director-photo";
    else if (person.id === "2") photoClass = "sahmurad-photo";
    else if (person.id === "3") photoClass = "ismayil-photo";
    else if (person.id === "7") photoClass = "babek-photo";
    else if (person.id === "9") photoClass = "sekine-photo";
    else if (person.id === "11") photoClass = "ceyhun-photo";
    else if (person.id === "12") photoClass = "seide-photo";
    else if (person.id === "13" || (person.img && person.img.includes("fizuli"))) photoClass = "fizuli-photo";
    else if (person.id === "14") photoClass = "resmiyye-photo";
    else if (person.id === "16") photoClass = "vefa-photo";
    else if (person.id === "18") photoClass = "gunay-photo";
    else if (person.id === "19") photoClass = "azer-photo";
    else if (person.id === "20") photoClass = "leman-photo";
    else if (person.id === "22") photoClass = "aynur-photo";
    else if (person.id === "23") photoClass = "yegane-photo";
    else if (person.id === "24") photoClass = "natiq-photo";
    else if (person.id === "25") photoClass = "sevda-photo";
    else if (person.id === "26") photoClass = "selale-photo";`;

if (code.includes(oldPhotoClassBlock)) {
  code = code.replace(oldPhotoClassBlock, newPhotoClassBlock);
  console.log('photoClass updated!');
} else {
  console.log('oldPhotoClassBlock not found, checking alternatives...');
}

// 7. Update wingAdminStaff to include 26
code = code.replace(
  '["13", "19", "16", "20", "22", "18"].includes(p.id)',
  '["13", "19", "16", "20", "22", "18", "26"].includes(p.id)'
);

fs.writeFileSync(targetFile, code, 'utf8');
fs.writeFileSync('/Users/konul/Documents/esas2 copy 2/script.js', code, 'utf8');
console.log('Both script files successfully written!');

