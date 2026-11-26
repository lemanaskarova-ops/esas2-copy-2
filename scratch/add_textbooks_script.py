with open("script.js", "r", encoding="utf-8") as f:
    js = f.read()

# Add i18n keys for textbooks
az_i18n_target = 'science_tab_all: "Bütün Nəşrlər (23)",'
az_i18n_add = '''science_tab_all: "Bütün Nəşrlər (23)",
    science_tab_textbooks: "📚 Dərslik və Dərs Vəsaitləri (8)",
    science_tb_kicker: "🏛️ RƏSMİ QEYDİYYAT REYESTRİ · 2025/2026 – 2026/2027",
    science_tb_title: "Kollec Əməkdaşlarının Nəşr Olunan Dərslik və Dərs Vəsaitləri",
    science_tb_desc: "Azərbaycan Respublikası Elm və Təhsil Nazirliyinin müvafiq qrifləri ilə təsdiq olunmuş və Bakı Dövlət Rabitə və Nəqliyyat Kolleci əməkdaşları tərəfindən 2025/2026 və 2026/2027-ci tədris illərində nəşr edilmiş rəsmi dərsliklər və tədris vəsaitlərinin tam dövlət reyestri.",
    science_tb_view_cards: "Kartlar",
    science_tb_view_table: "Rəsmi Cədvəl",
    science_tb_filter_derslik: "Qrifli Dərsliklər",
    science_tb_filter_vesait: "Dərs Vəsaitləri",
    science_tb_stat1: "Nazirlik Qrifi İlə",
    science_tb_stat2: "Tədris-Metodik Vəsait",
    science_tb_stat3: "Rəhbərlik & Müəllimlər",
    science_tb_stat4: "Tədris İlləri Nəşri",'''

assert az_i18n_target in js, "az_i18n_target not found in script.js"
js = js.replace(az_i18n_target, az_i18n_add, 1)

en_i18n_target = 'science_tab_all: "All Publications (23)",'
en_i18n_add = '''science_tab_all: "All Publications (23)",
    science_tab_textbooks: "📚 Textbooks & Study Guides (8)",
    science_tb_kicker: "🏛️ OFFICIAL REGISTRY · 2025/2026 – 2026/2027",
    science_tb_title: "Textbooks and Study Guides Published by College Faculty",
    science_tb_desc: "Official state register of textbooks and study guides approved by the Ministry of Science and Education of the Republic of Azerbaijan and published by the faculty of Baku State College of Communications and Transport for the 2025/2026 and 2026/2027 academic years.",
    science_tb_view_cards: "Cards",
    science_tb_view_table: "Official Table",
    science_tb_filter_derslik: "Approved Textbooks",
    science_tb_filter_vesait: "Study Guides",
    science_tb_stat1: "Ministry Approved",
    science_tb_stat2: "Curricular Guides",
    science_tb_stat3: "Leadership & Faculty",
    science_tb_stat4: "Academic Years",'''

assert en_i18n_target in js, "en_i18n_target not found in script.js"
js = js.replace(en_i18n_target, en_i18n_add, 1)

ru_i18n_target = 'science_tab_all: "Все публикации (23)",'
ru_i18n_add = '''science_tab_all: "Все публикации (23)",
    science_tab_textbooks: "📚 Учебники и Учебные Пособия (8)",
    science_tb_kicker: "🏛️ ОФИЦИАЛЬНЫЙ РЕЕСТР · 2025/2026 – 2026/2027",
    science_tb_title: "Учебники и учебные пособия, изданные сотрудниками колледжа",
    science_tb_desc: "Официальный государственный реестр учебников и учебных пособий, утвержденных соответствующими грифами Министерства науки и образования Азербайджанской Республики и изданных сотрудниками Бакинского государственного колледжа связи и транспорта в 2025/2026 и 2026/2027 учебных годах.",
    science_tb_view_cards: "Карточки",
    science_tb_view_table: "Официальная Таблица",
    science_tb_filter_derslik: "Учебники с грифом",
    science_tb_filter_vesait: "Учебные пособия",
    science_tb_stat1: "С грифом министерства",
    science_tb_stat2: "Учебно-методические",
    science_tb_stat3: "Руководство и преподаватели",
    science_tb_stat4: "Учебные годы издания",'''

assert ru_i18n_target in js, "ru_i18n_target not found in script.js"
js = js.replace(ru_i18n_target, ru_i18n_add, 1)

# Now add collegeTextbooksData and initCollegeTextbooksModule right before initScienceSection finishes or at end of script
textbooks_module_code = '''
/* ══════════════════════════════════════════════════════════════════
 * BDRNK — OFFICIAL TEXTBOOKS & STUDY GUIDES MODULE (2025/2026 - 2026/2027)
 * Extracted from official register: "Dərslik və dərs vəsaiti.pdf"
 * ══════════════════════════════════════════════════════════════════ */
(function initCollegeTextbooksModule() {
  const collegeTextbooksData = window.__bdrnkCollegeTextbooks = [
    {
      no: 1,
      title_az: "Xətti cəbr və riyazi analiz",
      title_en: "Linear Algebra and Mathematical Analysis",
      title_ru: "Линейная алгебра и математический анализ",
      authors_az: "Səbuhi Qurbanov Yusif, Suzanna Alıyeva Mirzalı",
      authors_en: "Sabuhi Gurbanov Yusif, Susanna Aliyeva Mirzali",
      authors_ru: "Сабухи Гурбанов Юсиф оглы, Сусанна Алиева Мирзалы гызы",
      roles_az: "1. BDRNK publik hüquqi şəxsin direktoru · 2. Müəllim / Ümumtəhsil fənn birləşməsi",
      roles_en: "1. Director of BDRNK · 2. Teacher / General Education Department",
      roles_ru: "1. Директор БГКСТ · 2. Преподаватель / ФБК общего образования",
      type_az: "Dərslik",
      type_en: "Textbook",
      type_ru: "Учебник",
      type_code: "derslik",
      qrif: "3-29/3-2-269 F/2026",
      qrif_badge: "Qrifli Rəsmi Dərslik",
      dept_az: "Ümumtəhsil fənn birləşməsi",
      dept_en: "General Education Department",
      dept_ru: "ФБК общего образования",
      icon: "📐",
      year: "2026"
    },
    {
      no: 2,
      title_az: "Riyaziyyat",
      title_en: "Mathematics",
      title_ru: "Математика",
      authors_az: "Suzanna Alıyeva Mirzalı",
      authors_en: "Susanna Aliyeva Mirzali",
      authors_ru: "Сусанна Алиева Мирзалы гызы",
      roles_az: "Müəllim / Ümumtəhsil fənn birləşməsi",
      roles_en: "Teacher / General Education Department",
      roles_ru: "Преподаватель / ФБК общего образования",
      type_az: "Dərslik",
      type_en: "Textbook",
      type_ru: "Учебник",
      type_code: "derslik",
      qrif: "3-29/3-2-734F/2025",
      qrif_badge: "Qrifli Rəsmi Dərslik",
      dept_az: "Ümumtəhsil fənn birləşməsi",
      dept_en: "General Education Department",
      dept_ru: "ФБК общего образования",
      icon: "🔢",
      year: "2026"
    },
    {
      no: 3,
      title_az: "Menecment",
      title_en: "Management",
      title_ru: "Менеджмент",
      authors_az: "İlahə Abbaslı Akif",
      authors_en: "Ilaha Abbasli Akif",
      authors_ru: "Илаха Аббаслы Акиф кызы",
      roles_az: "Müəllim / Poçt rabitəsi və iqtisadiyyat",
      roles_en: "Teacher / Postal Communications & Economics",
      roles_ru: "Преподаватель / Почтовая связь и экономика",
      type_az: "Dərslik",
      type_en: "Textbook",
      type_ru: "Учебник",
      type_code: "derslik",
      qrif: "3-29/3-2-313F/2025",
      qrif_badge: "Qrifli Rəsmi Dərslik",
      dept_az: "Poçt rabitəsi və iqtisadiyyat",
      dept_en: "Postal Communications & Economics",
      dept_ru: "Почтовая связь и экономика",
      icon: "📊",
      year: "2026"
    },
    {
      no: 4,
      title_az: "Fizika",
      title_en: "Physics",
      title_ru: "Физика",
      authors_az: "Ramilə Paşayeva Rza",
      authors_en: "Ramila Pashayeva Rza",
      authors_ru: "Рамила Пашаева Рза кызы",
      roles_az: "Müəllim / Ümumtəhsil fənn birləşməsi",
      roles_en: "Teacher / General Education Department",
      roles_ru: "Преподаватель / ФБК общего образования",
      type_az: "Dərs vəsaiti",
      type_en: "Study Guide",
      type_ru: "Учебное пособие",
      type_code: "vesait",
      qrif: "—",
      qrif_badge: "Tədris Dərs Vəsaiti",
      dept_az: "Ümumtəhsil fənn birləşməsi",
      dept_en: "General Education Department",
      dept_ru: "ФБК общего образования",
      icon: "⚛️",
      year: "2026"
    },
    {
      no: 5,
      title_az: "Ümumi kimya",
      title_en: "General Chemistry",
      title_ru: "Общая химия",
      authors_az: "Rəhimə Şəkərova Vahid",
      authors_en: "Rahima Shakarova Vahid",
      authors_ru: "Рахима Шакарова Вахид кызы",
      roles_az: "Müəllim / Ümumtəhsil fənn birləşməsi",
      roles_en: "Teacher / General Education Department",
      roles_ru: "Преподаватель / ФБК общего образования",
      type_az: "Dərs vəsaiti",
      type_en: "Study Guide",
      type_ru: "Учебное пособие",
      type_code: "vesait",
      qrif: "—",
      qrif_badge: "Tədris Dərs Vəsaiti",
      dept_az: "Ümumtəhsil fənn birləşməsi",
      dept_en: "General Education Department",
      dept_ru: "ФБК общего образования",
      icon: "🧪",
      year: "2026"
    },
    {
      no: 6,
      title_az: "İstehlakçı davranışları",
      title_en: "Consumer Behavior",
      title_ru: "Поведение потребителей",
      authors_az: "Gülnarə Məmmədova Muxtar",
      authors_en: "Gulnara Mammadova Mukhtar",
      authors_ru: "Гюльнара Мамедова Мухтар кызы",
      roles_az: "Müəllim / Poçt rabitəsi və iqtisadiyyat",
      roles_en: "Teacher / Postal Communications & Economics",
      roles_ru: "Преподаватель / Почтовая связь и экономика",
      type_az: "Dərs vəsaiti",
      type_en: "Study Guide",
      type_ru: "Учебное пособие",
      type_code: "vesait",
      qrif: "—",
      qrif_badge: "Tədris Dərs Vəsaiti",
      dept_az: "Poçt rabitəsi və iqtisadiyyat",
      dept_en: "Postal Communications & Economics",
      dept_ru: "Почтовая связь и экономика",
      icon: "🛍️",
      year: "2026"
    },
    {
      no: 7,
      title_az: "Fizika",
      title_en: "Physics",
      title_ru: "Физика",
      authors_az: "Günel Mirzəyeva Mahir, Cəvahir Mürşüdova Paşa",
      authors_en: "Gunel Mirzayeva Mahir, Javahir Murshudova Pasha",
      authors_ru: "Гюнель Мирзаева Махир кызы, Джавахир Муршудова Паша кызы",
      roles_az: "Müəllim / Ümumtəhsil fənn birləşməsi",
      roles_en: "Teacher / General Education Department",
      roles_ru: "Преподаватель / ФБК общего образования",
      type_az: "Dərslik",
      type_en: "Textbook",
      type_ru: "Учебник",
      type_code: "derslik",
      qrif: "3-29/3-2-233 F/2024",
      qrif_badge: "Qrifli Rəsmi Dərslik",
      dept_az: "Ümumtəhsil fənn birləşməsi",
      dept_en: "General Education Department",
      dept_ru: "ФБК общего образования",
      icon: "🔬",
      year: "2026"
    },
    {
      no: 8,
      title_az: "İnformatika",
      title_en: "Informatics & Computer Science",
      title_ru: "Информатика",
      authors_az: "İlkin Rəhmətov Soltan, Leyla Əfəndizadə Niyazi",
      authors_en: "Ilkin Rahmatov Soltan, Leyla Afandizade Niyazi",
      authors_ru: "Илькин Рахметов Солтан оглы, Лейла Эфендизаде Ниязи кызы",
      roles_az: "Müəllim / İnformatika fənn birləşməsi",
      roles_en: "Teacher / Informatics Department",
      roles_ru: "Преподаватель / ФБК информатики",
      type_az: "Dərs vəsaiti",
      type_en: "Study Guide",
      type_ru: "Учебное пособие",
      type_code: "vesait",
      qrif: "—",
      qrif_badge: "Tədris Dərs Vəsaiti",
      dept_az: "İnformatika fənn birləşməsi",
      dept_en: "Informatics Department",
      dept_ru: "ФБК информатики",
      icon: "💻",
      year: "2026"
    }
  ];

  let currentTbFilter = "all";
  let currentTbView = "cards";

  function getLoc(item, field) {
    const lang = typeof currentLang !== "undefined" ? currentLang : "az";
    return item[field + "_" + lang] || item[field + "_az"] || item[field] || "";
  }

  function renderCards() {
    const grid = document.getElementById("science-tb-cards-grid");
    if (!grid) return;

    const filtered = collegeTextbooksData.filter((b) => {
      if (currentTbFilter === "all") return true;
      return b.type_code === currentTbFilter;
    });

    grid.innerHTML = filtered.map((b) => {
      const title = getLoc(b, "title");
      const authors = getLoc(b, "authors");
      const roles = getLoc(b, "roles");
      const type = getLoc(b, "type");
      const dept = getLoc(b, "dept");
      const typeClass = b.type_code === "derslik" ? "type-derslik" : "type-vesait";
      const qrifHtml = b.qrif && b.qrif !== "—"
        ? `<div class="science-tb-qrif-row"><span class="science-tb-qrif-tag">🔖 Qrif №: ${b.qrif}</span></div>`
        : `<div class="science-tb-qrif-row"><span class="science-tb-qrif-tag" style="background:rgba(16,185,129,0.08); color:#059669; border-color:rgba(16,185,129,0.3);">📘 Kollec Təsdiqli Vəsait</span></div>`;

      return `
        <div class="science-tb-card">
          <div class="science-tb-card-top">
            <span class="science-tb-type-pill ${typeClass}">${type}</span>
            <span class="science-tb-year-badge">№ ${b.no} · ${b.year}</span>
          </div>
          <h4 class="science-tb-book-title">${b.icon} ${title}</h4>
          ${qrifHtml}
          <div class="science-tb-authors">👤 ${authors}</div>
          <div class="science-tb-roles">${roles}</div>
          <div class="science-tb-card-footer">
            <span>🏛️ ${dept}</span>
            <span>📅 ${b.year}</span>
          </div>
        </div>
      `;
    }).join("");
  }

  function renderTable() {
    const wrap = document.getElementById("science-tb-table-wrap");
    if (!wrap) return;

    const filtered = collegeTextbooksData.filter((b) => {
      if (currentTbFilter === "all") return true;
      return b.type_code === currentTbFilter;
    });

    const lang = typeof currentLang !== "undefined" ? currentLang : "az";
    const thNo = lang === "en" ? "№" : lang === "ru" ? "№" : "№";
    const thAuthor = lang === "en" ? "Author(s)" : lang === "ru" ? "Ф.И.О. сотрудника" : "Əməkdaşın adı, soyadı, ata adı";
    const thRole = lang === "en" ? "Position / Department" : lang === "ru" ? "Должность / Объединение" : "Vəzifəsi / Fənn birləşməsi";
    const thType = lang === "en" ? "Type" : lang === "ru" ? "Тип издания" : "Dərslik / dərs vəsaiti";
    const thQrif = lang === "en" ? "Stamp №" : lang === "ru" ? "Гриф №" : "Qrif №";
    const thTitle = lang === "en" ? "Title" : lang === "ru" ? "Название" : "Vəsaitin adı";
    const thYear = lang === "en" ? "Year" : lang === "ru" ? "Год" : "İl";

    wrap.innerHTML = `
      <table class="science-tb-table">
        <thead>
          <tr>
            <th style="width: 40px;">${thNo}</th>
            <th>${thAuthor}</th>
            <th>${thRole}</th>
            <th style="width: 130px;">${thType}</th>
            <th style="width: 170px;">${thQrif}</th>
            <th>${thTitle}</th>
            <th style="width: 70px;">${thYear}</th>
          </tr>
        </thead>
        <tbody>
          ${filtered.map((b) => {
            const title = getLoc(b, "title");
            const authors = getLoc(b, "authors");
            const roles = getLoc(b, "roles");
            const type = getLoc(b, "type");
            const typePill = b.type_code === "derslik" 
              ? `<span class="science-tb-type-pill type-derslik">${type}</span>`
              : `<span class="science-tb-type-pill type-vesait">${type}</span>`;
            const qrifText = b.qrif !== "—" ? `<strong>${b.qrif}</strong>` : `<span style="color:var(--text-dim);">—</span>`;

            return `
              <tr>
                <td style="font-weight: 800; text-align: center;">${b.no}</td>
                <td><strong>${authors}</strong></td>
                <td style="font-size: 0.8rem;">${roles}</td>
                <td>${typePill}</td>
                <td style="font-family: var(--font-mono, monospace); font-size: 0.76rem;">${qrifText}</td>
                <td><strong>${b.icon} ${title}</strong></td>
                <td style="font-weight: 700; text-align: center;">${b.year}</td>
              </tr>
            `;
          }).join("")}
        </tbody>
      </table>
    `;
  }

  function updateView() {
    const grid = document.getElementById("science-tb-cards-grid");
    const wrap = document.getElementById("science-tb-table-wrap");
    if (!grid || !wrap) return;

    if (currentTbView === "cards") {
      grid.style.display = "grid";
      wrap.style.display = "none";
      renderCards();
    } else {
      grid.style.display = "none";
      wrap.style.display = "block";
      renderTable();
    }
  }

  function init() {
    renderCards();
    renderTable();
    updateView();

    // View switcher buttons (cards / table)
    const viewBtns = document.querySelectorAll(".science-tb-view-btn[data-tb-view]");
    viewBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        viewBtns.forEach((b) => {
          b.classList.remove("active");
          b.classList.remove("bg-white", "dark:bg-[#0a2240]", "text-slate-900", "dark:text-white", "shadow-xs");
          b.classList.add("text-slate-600", "dark:text-slate-400");
        });
        btn.classList.add("active");
        btn.classList.remove("text-slate-600", "dark:text-slate-400");
        btn.classList.add("bg-white", "dark:bg-[#0a2240]", "text-slate-900", "dark:text-white", "shadow-xs");
        currentTbView = btn.getAttribute("data-tb-view");
        updateView();
      });
    });

    // Filter buttons (all / derslik / vesait)
    const filterBtns = document.querySelectorAll(".science-tb-filter-btn[data-tb-filter]");
    filterBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        filterBtns.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        currentTbFilter = btn.getAttribute("data-tb-filter");
        updateView();
      });
    });

    // Main science tab link for textbooks
    const mainTbTabBtn = document.getElementById("science-tab-tb-btn");
    if (mainTbTabBtn) {
      mainTbTabBtn.addEventListener("click", () => {
        const sec = document.getElementById("science-textbooks-section");
        if (sec) {
          sec.scrollIntoView({ behavior: "smooth", block: "start" });
          sec.style.boxShadow = "0 0 0 3px rgba(184, 147, 74, 0.4)";
          setTimeout(() => {
            sec.style.boxShadow = "";
          }, 2000);
        }
      });
    }

    document.addEventListener("languageChanged", () => {
      updateView();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
'''

js += "\n" + textbooks_module_code

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)

print("script.js updated with collegeTextbooksData and initCollegeTextbooksModule!")
