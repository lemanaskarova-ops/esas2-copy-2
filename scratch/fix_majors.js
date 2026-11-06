const fs = require('fs');

const majorIconsBlock = `  const majorIcons = {
    "040406": "📊", // Mühasibat uçotu
    "040554": "📮", // Poçt rabitəsi
    "040556": "📻", // Radio, televiziya vasitə və qurğuları
    "040405": "📈", // Marketinq
    "040544": "📱", // Mobil şəbəkə sistemləri və operatorluğu
    "040565": "🌐", // Telekommunikasiya şəbəkələri və xətləri
    "040508": "📡", // Çoxkanallı telekommunikasiya sistemlərinin istismarı
    "040572": "🚃", // Vaqon və refrijerator sistemləri
    "040552": "🚚", // Nəqliyyatın logistikası
    "040550": "🚗", // Nəqliyyat vasitələrinin texniki istismarı
    "040518": "🌱", // Ətraf mühitin mühafizəsi və bərpası
    "040529": "💻", // Kompüter sistemləri və kompleksləri
    "040533": "🛠️", // Kompüter şəbəkə avadanlıqlarının təmiri və servisi
    "040532": "🛡️", // Kompüter şəbəkələri və şəbəkə inzibatçılığı
  };`;

function fixFile(filePath) {
  let code = fs.readFileSync(filePath, 'utf8');

  // 1. Replace renderMajorCards with renderTableRows and majorIcons
  const oldMajorCardsPattern = /\/\/ İxtisaslar Məlumatı[\s\S]*?const renderMajorCards = \([\s\S]*?\n    \};/;
  
  const newTableRowsBlock = `// İxtisaslar Məlumatı (Müasir Akademik Cədvəl Dizaynı)
${majorIconsBlock}

    const eyaniMajors = staffData.majors.eyani || [];
    const qiyabiMajors = staffData.majors.qiyabi || [];

    function renderTableRows(list, mode) {
      return list
        .map((m, idx) => {
          const name = m[\`name_\${currentLang}\`] || m.name_az;
          const field = m[\`field_\${currentLang}\`] || m.field_az;
          const icon = majorIcons[m.code] || "📘";
          const modeLabel =
            mode === "eyani"
              ? (currentLang === "en" ? "Full-time" : currentLang === "ru" ? "Очно" : "Əyani")
              : (currentLang === "en" ? "Part-time" : currentLang === "ru" ? "Заочно" : "Qiyabi");
          const subDegree =
            currentLang === "en" ? "Sub-bachelor" : currentLang === "ru" ? "Суббакалавр" : "Subbakalavr";

          return \`
            <tr class="major-row" data-code="\${m.code}">
              <td class="td-num">\${idx + 1}</td>
              <td class="td-code" data-label="\${gT("th_code") || "Kod"}">
                <span class="major-code-pill">\${m.code}</span>
              </td>
              <td class="td-name" data-label="\${gT("th_major") || "İxtisas"}">
                <div class="major-name-wrap">
                  <span class="major-row-icon">\${icon}</span>
                  <div class="major-title-group">
                    <span class="major-row-title">\${name}</span>
                    <span class="major-row-sub">\${m.code} · \${field}</span>
                  </div>
                </div>
              </td>
              <td class="td-field" data-label="\${gT("th_field") || "Sahə"}">
                <span class="major-field-chip">\${field}</span>
              </td>
              <td class="td-degree" data-label="\${gT("th_degree") || "Dərəcə"}">
                <div class="major-degree-badge">
                  <span class="degree-sub">\${subDegree}</span>
                  <span class="degree-mode mode-\${mode}">\${modeLabel}</span>
                </div>
              </td>
            </tr>\`;
        })
        .join("");
    }`;

  if (oldMajorCardsPattern.test(code)) {
    code = code.replace(oldMajorCardsPattern, newTableRowsBlock);
    console.log("Replaced renderMajorCards in", filePath);
  } else {
    console.log("oldMajorCardsPattern not matched in", filePath);
  }

  // 2. Replace tree-majors-section in treeCanvas.innerHTML
  const oldTreeMajorsPattern = /<!-- ═══ TƏDRİS OLUNAN İXTİSASLAR VİTRİNİ ═══ -->[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*`;/;
  const newTreeMajorsBlock = `<!-- ═══ TƏDRİS OLUNAN İXTİSASLAR VİTRİNİ (ACADEMIC CATALOG) ═══ -->
      <div class="tree-majors-section" id="tree-majors-block">
        <div class="majors-catalog-header">
          <div class="majors-header-badge">
            <span>🎓</span> <span>\${gT("struct_majors_badge") || "DÖVLƏT STANDARTLI TƏDRİS PROQRAMLARI"}</span>
          </div>
          <h3 class="majors-catalog-title">\${gT("struct_majors_heading") || "Kollecdə Tədris Olunan İxtisaslar"}</h3>
          <p class="majors-catalog-desc">\${gT("struct_majors_desc") || "Dövlət təhsil standartlarına uyğun əyani və qiyabi orta ixtisas təhsili proqramları (19 İxtisas)"}</p>
          <div class="majors-catalog-tabs" role="tablist">
            <button type="button" class="majors-tab-btn active" data-major-view="eyani">
              <span>📘 \${gT("major_eyani_tab") || "Əyani Təhsil"}</span>
              <span class="tab-count">\${eyaniMajors.length}</span>
            </button>
            <button type="button" class="majors-tab-btn" data-major-view="qiyabi">
              <span>📗 \${gT("major_qiyabi_tab") || "Qiyabi Təhsil"}</span>
              <span class="tab-count">\${qiyabiMajors.length}</span>
            </button>
          </div>
        </div>

        <div class="majors-pane active" id="majors-pane-eyani">
          <div class="majors-table-container">
            <table class="majors-catalog-table">
              <thead>
                <tr>
                  <th class="th-num">№</th>
                  <th class="th-code">\${gT("th_code") || "İxtisas Kodu"}</th>
                  <th class="th-name">\${gT("th_major") || "İxtisasın Tam Adı"}</th>
                  <th class="th-field">\${gT("th_field") || "Tədris Sahəsi"}</th>
                  <th class="th-degree">\${gT("th_degree") || "Təhsil Pilləsi"}</th>
                </tr>
              </thead>
              <tbody>
                \${renderTableRows(eyaniMajors, "eyani")}
              </tbody>
            </table>
          </div>
        </div>

        <div class="majors-pane" id="majors-pane-qiyabi">
          <div class="majors-table-container">
            <table class="majors-catalog-table">
              <thead>
                <tr>
                  <th class="th-num">№</th>
                  <th class="th-code">\${gT("th_code") || "İxtisas Kodu"}</th>
                  <th class="th-name">\${gT("th_major") || "İxtisasın Tam Adı"}</th>
                  <th class="th-field">\${gT("th_field") || "Tədris Sahəsi"}</th>
                  <th class="th-degree">\${gT("th_degree") || "Təhsil Pilləsi"}</th>
                </tr>
              </thead>
              <tbody>
                \${renderTableRows(qiyabiMajors, "qiyabi")}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    \`;`;

  if (oldTreeMajorsPattern.test(code)) {
    code = code.replace(oldTreeMajorsPattern, newTreeMajorsBlock);
    console.log("Replaced tree-majors-section in", filePath);
  } else {
    console.log("oldTreeMajorsPattern not matched in", filePath);
  }

  // 3. Replace Majors switcher tabs event listeners
  const oldSwitcherPattern = /\/\/ Majors switcher tabs in tree canvas[\s\S]*?treeCanvas\.querySelectorAll\("\.tree-major-btn"\)[\s\S]*?\}\);[\s\S]*?\}\);/;
  const newSwitcherBlock = `// Majors switcher tabs in tree canvas
    treeCanvas.querySelectorAll(".majors-tab-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const view = btn.dataset.majorView;
        treeCanvas.querySelectorAll(".majors-tab-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        treeCanvas.querySelectorAll(".majors-pane").forEach((p) => p.classList.remove("active"));
        const target = treeCanvas.querySelector(\`#majors-pane-\${view}\`);
        if (target) target.classList.add("active");
      });
    });`;

  if (oldSwitcherPattern.test(code)) {
    code = code.replace(oldSwitcherPattern, newSwitcherBlock);
    console.log("Replaced switcher listeners in", filePath);
  } else {
    console.log("oldSwitcherPattern not matched in", filePath);
  }

  fs.writeFileSync(filePath, code, 'utf8');
}

fixFile('/Users/konul/Documents/esas2 copy 2/scratch/script_working_backup.js');
fixFile('/Users/konul/Documents/esas2 copy 2/script.js');
console.log("Done!");

