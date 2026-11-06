const fs = require('fs');

const fbkListBlock = `  const fbkList = [
    {
      id: "fbk-1",
      code: "FBK-01",
      icon: "💻",
      status: "Aktiv",
      title_az: "İnformatika və Kompüter Sistemləri",
      title_en: "Informatics and Computer Systems",
      title_ru: "Информатика и компьютерные системы",
      desc_az: "Kompüter sistemlərinin təmiri, proqramlaşdırma, verilənlər bazası və veb-texnologiyalar üzrə ixtisas fənləri.",
      desc_en: "Specialized courses in computer hardware maintenance, programming, database management, and web technologies.",
      desc_ru: "Профильные дисциплины по ремонту компьютерных систем, программированию, базам данных и веб-технологиям.",
      disciplines_az: ["İnformatika", "Verilənlər Bazası", "Kompüter Qrafikası", "Proqramlaşdırma", "Şəbəkə Təminatı"],
      chair_az: "Teyyubə Bağırova",
      chair_en: "Teyyuba Baghirova",
      chair_ru: "Тейюба Багирова"
    },
    {
      id: "fbk-2",
      code: "FBK-02",
      icon: "📡",
      status: "Aktiv",
      title_az: "Telekommunikasiya və Rabitə Xətləri",
      title_en: "Telecommunications and Network Lines",
      title_ru: "Телекоммуникации и линии связи",
      desc_az: "Simsiz və optik rabitə sistemləri, şəbəkə inzibatçılığı və siqnalların ötürülməsi fənn birləşməsi.",
      desc_en: "Curriculum focusing on wireless and optical networks, telecom systems, and transmission technologies.",
      desc_ru: "Программы по беспроводным и оптическим сетям связи, администрированию и технологиям передачи сигналов.",
      disciplines_az: ["Telekommunikasiya", "Optik Rabitə", "Mobil Şəbəkələr", "Radiotexnika", "Kabel Sistemləri"],
      chair_az: "Sevda Bağızadə",
      chair_en: "Sevda Bagizada",
      chair_ru: "Севда Багизаде"
    },
    {
      id: "fbk-3",
      code: "FBK-03",
      icon: "📦",
      status: "Aktiv",
      title_az: "Poçt Rabitəsi və İqtisadiyyat",
      title_en: "Postal Communications and Economics",
      title_ru: "Почтовая связь и экономика",
      desc_az: "Poçt xidmətlərinin təşkili, anbar logistikası, mühasibat uçotu və maliyyə-bank əməliyyatları.",
      desc_en: "Comprehensive training in postal logistics, warehousing, financial accounting, and modern banking services.",
      desc_ru: "Комплексное обучение почтовой логистике, складированию, бухгалтерскому учету и банковским операциям.",
      disciplines_az: ["Poçt Əməliyyatları", "Anbar Logistikası", "Mühasibat Uçotu", "Bank İşi", "Maliyyə"],
      chair_az: "Natiq Əhmədov",
      chair_en: "Natig Ahmadov",
      chair_ru: "Натиг Ахмедов"
    },
    {
      id: "fbk-4",
      code: "FBK-04",
      icon: "🔌",
      status: "Aktiv",
      title_az: "Elektrotexnika və Sxematexnika",
      title_en: "Electrical Engineering & Schematics",
      title_ru: "Электротехника и схемотехника",
      desc_az: "Elektron qurğular, dövrələr, elektrik ölçmələri və mikroprosessor texnikasının əsasları.",
      desc_en: "Theoretical and practical instruction in circuit design, electrical apparatus, and microprocessors.",
      desc_ru: "Теоретические и практические занятия по схемотехнике, электрическим измерениям и микропроцессорам.",
      disciplines_az: ["Sxematexnika", "Elektrik Ölçmələri", "Mikroprosessorlar", "Elektronika", "Rəqəmsal Texnika"],
      chair_az: "Kollec Metodik Şurası",
      chair_en: "College Methodological Board",
      chair_ru: "Методический совет"
    },
    {
      id: "fbk-5",
      code: "FBK-05",
      icon: "🚘",
      status: "Aktiv",
      title_az: "Ümumtexnika və Nəqliyyat",
      title_en: "General Engineering & Transport",
      title_ru: "Общая техника и транспорт",
      desc_az: "Avtomobil və dəmiryol nəqliyyatının istismarı, yol hərəkətinin təşkili və texniki diaqnostika.",
      desc_en: "Operation of transport vehicles, traffic coordination, diagnostic testing, and technical safety.",
      desc_ru: "Эксплуатация транспорта, организация дорожного движения, диагностика и техническая безопасность.",
      disciplines_az: ["Nəqliyyat Diaqnostikası", "Yol Hərəkəti Təşkili", "Texniki Mexanika", "Materialşünaslıq", "Logistika"],
      chair_az: "Babək Quliyev",
      chair_en: "Babak Guliyev",
      chair_ru: "Бабек Гулиев"
    },
    {
      id: "fbk-6",
      code: "FBK-06",
      icon: "📖",
      status: "Aktiv",
      title_az: "Azərbaycan Dili və Ədəbiyyat",
      title_en: "Azerbaijani Language and Literature",
      title_ru: "Азербайджанский язык и литература",
      desc_az: "Ana dilimizin zənginliyi, nitq mədəniyyəti, klassik və müasir milli ədəbiyyat irsi.",
      desc_en: "Preservation of linguistic standards, academic rhetoric, and study of classical national literature.",
      desc_ru: "Культура речи, литературное наследие, грамматика и академическая риторика родного языка.",
      disciplines_az: ["Azərbaycan Dili", "Ədəbiyyat", "Nitq Mədəniyyəti", "İşgüzar Yazışmalar", "Azərbaycançılıq"],
      chair_az: "Ziba Səfərova",
      chair_en: "Ziba Safarova",
      chair_ru: "Зиба Сафарова"
    },
    {
      id: "fbk-7",
      code: "FBK-07",
      icon: "🏛️",
      status: "Aktiv",
      title_az: "Humanitar və İctimai Elmlər",
      title_en: "Humanities and Social Sciences",
      title_ru: "Гуманитарные и общественные науки",
      desc_az: "Azərbaycan tarixi, konstitusiya və hüququn əsasları, fəlsəfə və ictimai elmlər.",
      desc_en: "History of Azerbaijan, constitutional law fundamentals, civic ethics, and philosophy.",
      desc_ru: "История Азербайджана, основы конституционного права, гражданское право и философия.",
      disciplines_az: ["Azərbaycan Tarixi", "Hüququn Əsasları", "Fəlsəfə", "Multikulturalizm", "İctimaiyyət"],
      chair_az: "Səidə Quliyeva",
      chair_en: "Saida Guliyeva",
      chair_ru: "Саида Гулиева"
    },
    {
      id: "fbk-8",
      code: "FBK-08",
      icon: "🌍",
      status: "Aktiv",
      title_az: "Xarici Dillər",
      title_en: "Foreign Languages",
      title_ru: "Иностранные языки",
      desc_az: "Texniki və işgüzar ingilis dili, rus dili və beynəlxalq rabitə terminologiyası.",
      desc_en: "Technical English, Russian, cross-cultural communication, and professional telecom terminology.",
      desc_ru: "Технический и деловой английский, русский язык и терминология международных систем связи.",
      disciplines_az: ["İngilis Dili", "Rus Dili", "Texniki Tərcümə", "İşgüzar Ünsiyyət", "Akademik Yazı"],
      chair_az: "Aynur Əliyeva",
      chair_en: "Aynur Aliyeva",
      chair_ru: "Айнур Алиева"
    },
    {
      id: "fbk-9",
      code: "FBK-09",
      icon: "⚽",
      status: "Aktiv",
      title_az: "Dəqiq Elmlər, Fiziki Tərbiyə və ÇHQ",
      title_en: "Natural Sciences, Physical Ed. & Pre-Conscription",
      title_ru: "Точные науки, физвоспитание и ДПЮ",
      desc_az: "Tətbiqi riyaziyyat, fizika, kimya, hərbi vətənpərvərlik hazırlığı və tələbə idman nailiyyətləri.",
      desc_en: "Applied mathematics, physics, sports coaching, civil defense, and patriotic education.",
      desc_ru: "Прикладная математика, физика, военно-патриотическая подготовка, спорт и гражданская оборона.",
      disciplines_az: ["Riyaziyyat", "Fizika", "Fiziki Tərbiyə", "Çağırışaqədərki Hazırlıq", "Mülki Müdafiə"],
      chair_az: "Ramilə Paşayeva",
      chair_en: "Ramila Pashayeva",
      chair_ru: "Рамила Пашаева"
    }
  ];`;

const renderCommissionsGridBlock = `  // ─── 2. RENDER COMMISSIONS (9 FBK) GRID ────────────────────────────
  function renderCommissionsGrid() {
    const grid = document.getElementById("fbk-grid");
    if (!grid) return;
    grid.innerHTML = fbkList.map((fbk) => {
      const title = fbk[\`title_\${currentLang}\`] || fbk.title_az;
      const desc = fbk[\`desc_\${currentLang}\`] || fbk.desc_az;
      const chair = fbk[\`chair_\${currentLang}\`] || fbk.chair_az;
      const disciplines = fbk.disciplines_az || [];
      const viewLabel = currentLang === "en" ? "View Details →" : currentLang === "ru" ? "Подробнее →" : "Ətraflı Bax →";

      return \`
        <div class="fbk-card" data-fbk-id="\${fbk.id}">
          <div class="fbk-card-header">
            <div class="fbk-icon-wrap">
              <span class="fbk-icon">\${fbk.icon}</span>
            </div>
            <div class="fbk-meta-badge">
              <span class="fbk-code">\${fbk.code}</span>
              <span class="fbk-status-pill">\${fbk.status}</span>
            </div>
          </div>
          <h4 class="fbk-title">\${title}</h4>
          <p class="fbk-desc">\${desc}</p>
          <div class="fbk-disciplines">
            \${disciplines.map(d => \`<span class="fbk-chip">\${d}</span>\`).join("")}
          </div>
          <div class="fbk-card-footer">
            <span class="fbk-dept-link">👨‍🏫 Sədr: \${chair}</span>
            <span class="fbk-card-action">\${viewLabel}</span>
          </div>
        </div>
      \`;
    }).join("");

    // Modal detail click on fbk-card
    grid.querySelectorAll(".fbk-card").forEach((card) => {
      card.addEventListener("click", () => {
        const id = card.dataset.fbkId;
        const fbk = fbkList.find((f) => f.id === id);
        if (fbk && modal && modalGrid) {
          const modalContainer = modal.querySelector(".modal-container");
          if (modalContainer) modalContainer.classList.add("is-person-detail");
          if (modalTitle) modalTitle.textContent = fbk[\`title_\${currentLang}\`] || fbk.title_az;
          modalGrid.classList.remove("table-mode");
          modalGrid.classList.add("person-detail-active");

          const disciplines = fbk.disciplines_az || [];
          const chair = fbk[\`chair_\${currentLang}\`] || fbk.chair_az;
          const desc = fbk[\`desc_\${currentLang}\`] || fbk.desc_az;

          modalGrid.innerHTML = \`
            <div class="fbk-modal-detail" style="padding: 24px; color: var(--text);">
              <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 20px;">
                <div style="font-size: 2.5rem; width: 64px; height: 64px; border-radius: 16px; background: rgba(184, 147, 74, 0.15); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(184, 147, 74, 0.3);">\${fbk.icon}</div>
                <div>
                  <span style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--gold-light); font-weight: 700; background: rgba(184, 147, 74, 0.1); padding: 3px 10px; border-radius: 6px; border: 1px solid rgba(184, 147, 74, 0.25);">\${fbk.code}</span>
                  <h3 style="margin: 8px 0 4px; font-family: var(--font-display); font-size: 1.35rem; font-weight: 800;">\${fbk[\`title_\${currentLang}\`] || fbk.title_az}</h3>
                  <div style="color: var(--text-dim); font-size: 0.9rem;">👨‍🏫 <strong>Sədr:</strong> \${chair}</div>
                </div>
              </div>
              <p style="font-size: 0.95rem; line-height: 1.6; color: var(--text-dim); margin-bottom: 20px;">\${desc}</p>
              <div>
                <h5 style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--gold-light); margin-bottom: 10px;">Tədris olunan əsas fənlər:</h5>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                  \${disciplines.map(d => \`<span style="background: var(--surface); border: 1px solid var(--border); padding: 5px 12px; border-radius: 12px; font-size: 0.82rem; font-weight: 600;">\${d}</span>\`).join("")}
                </div>
              </div>
            </div>
          \`;
          modal.classList.add("active");
          modal.setAttribute("aria-hidden", "false");
          html.classList.add("modal-open");
        }
      });
    });
  }`;

function restoreFBK(filePath) {
  let code = fs.readFileSync(filePath, 'utf8');

  // 1. Fix variables in initStructureModule()
  code = code.replace(
    'const cardsPane = document.getElementById("struct-cards-view");',
    'const commissionsPane = document.getElementById("struct-commissions-view") || document.getElementById("struct-cards-view");'
  );

  // 2. Insert fbkList before renderTree if not present
  if (!code.includes('const fbkList = [')) {
    code = code.replace(
      '// ─── 1. RENDER ORGANIZATIONAL TREE VIEW ─────────────────────────────',
      `${fbkListBlock}\n\n  // ─── 1. RENDER ORGANIZATIONAL TREE VIEW ─────────────────────────────`
    );
  }

  // 3. Replace old renderCards() with renderCommissionsGrid()
  const renderCardsPattern = /\/\/ ─── 2\. RENDER CARDS VIEW \(In-Page\) ────────────────────────────────[\s\S]*?liveGrid\.appendChild\(card\);\s*\}\);\s*\}\s*\}/;
  if (renderCardsPattern.test(code)) {
    code = code.replace(renderCardsPattern, renderCommissionsGridBlock);
    console.log("Replaced renderCards with renderCommissionsGrid in", filePath);
  } else {
    console.log("renderCardsPattern not matched in", filePath);
  }

  // 4. Update switchView function
  const oldSwitchViewPattern = /function switchView\(view\) \{[\s\S]*?toggleCardsBtn\?\.addEventListener\("click", \(\) => switchView\("cards"\)\);/;
  const newSwitchViewBlock = `function switchView(view) {
    currentView = view;
    if (view === "tree") {
      toggleTreeBtn?.classList.add("active");
      toggleTreeBtn?.setAttribute("aria-selected", "true");
      toggleCardsBtn?.classList.remove("active");
      toggleCardsBtn?.setAttribute("aria-selected", "false");

      treePane?.classList.add("active");
      commissionsPane?.classList.remove("active");
      renderTree();
    } else {
      toggleCardsBtn?.classList.add("active");
      toggleCardsBtn?.setAttribute("aria-selected", "true");
      toggleTreeBtn?.classList.remove("active");
      toggleTreeBtn?.setAttribute("aria-selected", "false");

      commissionsPane?.classList.add("active");
      treePane?.classList.remove("active");
      renderCommissionsGrid();
    }
  }

  toggleTreeBtn?.addEventListener("click", () => switchView("tree"));
  toggleCardsBtn?.addEventListener("click", () => switchView("commissions"));`;

  if (oldSwitchViewPattern.test(code)) {
    code = code.replace(oldSwitchViewPattern, newSwitchViewBlock);
    console.log("Updated switchView in", filePath);
  } else {
    console.log("oldSwitchViewPattern not matched in", filePath);
  }

  // 5. Update search for commissions view
  code = code.replace(
    `const cards = liveGrid.querySelectorAll(".staff-card");`,
    `const cards = commissionsPane ? commissionsPane.querySelectorAll(".fbk-card") : [];`
  );

  // 6. Update language change listener and initial render
  code = code.replace(
    `window.addEventListener("appLanguageChanged", () => {\n    if (currentView === "tree") {\n      renderTree();\n    } else {\n      renderCards(currentCategory);\n    }\n  });\n\n  // Initial Tree render\n  renderTree();`,
    `window.addEventListener("appLanguageChanged", () => {\n    if (currentView === "tree") {\n      renderTree();\n    } else {\n      renderCommissionsGrid();\n    }\n  });\n\n  // Initial renders\n  renderTree();\n  renderCommissionsGrid();`
  );

  fs.writeFileSync(filePath, code, 'utf8');
}

restoreFBK('/Users/konul/Documents/esas2 copy 2/scratch/script_working_backup.js');
restoreFBK('/Users/konul/Documents/esas2 copy 2/script.js');
console.log("FBK restored successfully!");

