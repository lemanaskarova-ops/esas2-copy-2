const fs = require('fs');
const path = require('path');

const rootDir = '/Users/konul/Documents/esas2 copy 2';
const indexHtmlPath = path.join(rootDir, 'index.html');
const styleCssPath = path.join(rootDir, 'style.css');
const scriptJsPath = path.join(rootDir, 'script.js');
const backupJsPath = path.join(rootDir, 'scratch/script_working_backup.js');

// ══════════════════════════════════════════════════════════════════════
// 1. UPDATE script.js — CATEGORIES IN lecturesData & LOGIC
// ══════════════════════════════════════════════════════════════════════
let js = fs.readFileSync(scriptJsPath, 'utf8');

// Update categories for IDs:
// id 18, 19, 20, 21 -> "az-dili"
// id 22, 23, 24, 25 -> "edebiyyat"
// id 26 -> "biologiya"
// id 27 -> "gch"
// id 28, 29, 30, 31 -> "huquq"

// Update category for ID 18
js = js.replace(/id:\s*18,\s*title_az:\s*"Ana dili[^"]*",[^}]*?category:\s*"edebiyyat"/s, (m) => m.replace('"edebiyyat"', '"az-dili"'));
// Update category for ID 19
js = js.replace(/id:\s*19,\s*title_az:\s*"3 dəqiqədə söz birləşmələrinin[^"]*",[^}]*?category:\s*"edebiyyat"/s, (m) => m.replace('"edebiyyat"', '"az-dili"'));
// Update category for ID 20
js = js.replace(/id:\s*20,\s*title_az:\s*"Feilin qrammatik məna növlərinin[^"]*",[^}]*?category:\s*"edebiyyat"/s, (m) => m.replace('"edebiyyat"', '"az-dili"'));
// Update category for ID 21
js = js.replace(/id:\s*21,\s*title_az:\s*"İmtahan üçün vacib qaydalar və izah[^"]*",[^}]*?category:\s*"edebiyyat"/s, (m) => m.replace('"edebiyyat"', '"az-dili"'));

// Update category for ID 26 (Biologiya)
js = js.replace(/id:\s*26,\s*title_az:\s*"Biologiya fənnindən 513A qrupu ilə dərs[^"]*",[^}]*?category:\s*"huquq"/s, (m) => m.replace('"huquq"', '"biologiya"'));
// Update category for ID 27 (GCH)
js = js.replace(/id:\s*27,\s*title_az:\s*"Çağırışaqədərki hazırlıq fənni[^"]*",[^}]*?category:\s*"huquq"/s, (m) => m.replace('"huquq"', '"gch"'));

// Add i18n keys for new categories
const azI18nTarget = 'filter_telecom: "Telekommunikasiya",';
const azI18nReplace = `filter_telecom: "Telekommunikasiya",
    filter_azdili: "Azərbaycan Dili",
    filter_biologiya: "Biologiya",
    filter_gch: "Çağırışaqədərki Hazırlıq",`;

const enI18nTarget = 'filter_telecom: "Telecommunications",';
const enI18nReplace = `filter_telecom: "Telecommunications",
    filter_azdili: "Azerbaijani Language",
    filter_biologiya: "Biology",
    filter_gch: "Pre-Conscription Military Training",`;

const ruI18nTarget = 'filter_telecom: "Телекоммуникации",';
const ruI18nReplace = `filter_telecom: "Телекоммуникации",
    filter_azdili: "Азербайджанский язык",
    filter_biologiya: "Биология",
    filter_gch: "Допризывная подготовка",`;

if (js.includes(azI18nTarget) && !js.includes('filter_azdili: "Azərbaycan Dili"')) {
  js = js.replace(azI18nTarget, azI18nReplace);
}
if (js.includes(enI18nTarget) && !js.includes('filter_azdili: "Azerbaijani Language"')) {
  js = js.replace(enI18nTarget, enI18nReplace);
}
if (js.includes(ruI18nTarget) && !js.includes('filter_azdili: "Азербайджанский язык"')) {
  js = js.replace(ruI18nTarget, ruI18nReplace);
}

// Update getCategoryLabel in initLecturesModule
const oldGetCategoryLabel = `  function getCategoryLabel(cat) {
    const map = {
      informatika: gT("filter_informatika") || "İnformatika",
      telekommunikasiya: gT("filter_telecom") || "Telekommunikasiya",
      tarix: gT("filter_tarix") || "Tarix",
      edebiyyat: gT("filter_edebiyyat") || "Ədəbiyyat",
      huquq: gT("filter_huquq") || "Hüquq və Ümumtəhsil",
    };
    return map[cat] || cat;
  }`;

const newGetCategoryLabel = `  function getCategoryLabel(cat) {
    const map = {
      informatika: gT("filter_informatika") || "İnformatika və İKT",
      telekommunikasiya: gT("filter_telecom") || "Telekommunikasiya",
      tarix: gT("filter_tarix") || "Azərbaycan Tarixi",
      "az-dili": gT("filter_azdili") || "Azərbaycan Dili",
      edebiyyat: gT("filter_edebiyyat") || "Ədəbiyyat",
      huquq: gT("filter_huquq") || "Hüquq və Konstitusiya",
      biologiya: gT("filter_biologiya") || "Biologiya",
      gch: gT("filter_gch") || "Çağırışaqədərki Hazırlıq",
    };
    return map[cat] || cat;
  }`;

if (js.includes(oldGetCategoryLabel)) {
  js = js.replace(oldGetCategoryLabel, newGetCategoryLabel);
}

// Update updateDeptMetaLabels & count badges
const oldUpdateDeptMeta = `    // Update count badges
    const countMap = {
      "dept-count-all": lecturesData.length,
      "dept-count-informatika": lecturesData.filter((l) => l.category === "informatika").length,
      "dept-count-telekommunikasiya": lecturesData.filter((l) => l.category === "telekommunikasiya").length,
      "dept-count-tarix": lecturesData.filter((l) => l.category === "tarix").length,
      "dept-count-edebiyyat": lecturesData.filter((l) => l.category === "edebiyyat").length,
      "dept-count-huquq": lecturesData.filter((l) => l.category === "huquq").length,
    };`;

const newUpdateDeptMeta = `    // Update count badges
    const countMap = {
      "dept-count-all": lecturesData.length,
      "dept-count-informatika": lecturesData.filter((l) => l.category === "informatika").length,
      "dept-count-telekommunikasiya": lecturesData.filter((l) => l.category === "telekommunikasiya").length,
      "dept-count-tarix": lecturesData.filter((l) => l.category === "tarix").length,
      "dept-count-az-dili": lecturesData.filter((l) => l.category === "az-dili").length,
      "dept-count-edebiyyat": lecturesData.filter((l) => l.category === "edebiyyat").length,
      "dept-count-huquq": lecturesData.filter((l) => l.category === "huquq").length,
      "dept-count-biologiya": lecturesData.filter((l) => l.category === "biologiya").length,
      "dept-count-gch": lecturesData.filter((l) => l.category === "gch").length,
    };`;

if (js.includes(oldUpdateDeptMeta)) {
  js = js.replace(oldUpdateDeptMeta, newUpdateDeptMeta);
}

// Wire horizontal arrow buttons for lecture-dept-grid carousel
const oldFilterBadgesClick = `  // Filter badges click
  filterContainer.addEventListener("click", (e) => {
    const btn = e.target.closest(".filter-badge");
    if (!btn) return;
    setCategory(btn.getAttribute("data-filter"));
  });

  // Department cards click
  if (deptGrid) {
    deptGrid.addEventListener("click", (e) => {
      const card = e.target.closest(".lecture-dept-card");
      if (!card) return;
      setCategory(card.getAttribute("data-filter"));
    });
  }`;

const newFilterBadgesClick = `  // Filter badges click
  filterContainer.addEventListener("click", (e) => {
    const btn = e.target.closest(".filter-badge");
    if (!btn) return;
    setCategory(btn.getAttribute("data-filter"));
  });

  // Department cards click
  if (deptGrid) {
    deptGrid.addEventListener("click", (e) => {
      const card = e.target.closest(".lecture-dept-card");
      if (!card) return;
      setCategory(card.getAttribute("data-filter"));
      card.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    });
  }

  // Horizontal Slider Arrows for lecture departments
  const deptPrevBtn = document.getElementById("lecture-dept-prev");
  const deptNextBtn = document.getElementById("lecture-dept-next");
  if (deptPrevBtn && deptGrid) {
    deptPrevBtn.addEventListener("click", () => {
      deptGrid.scrollBy({ left: -280, behavior: "smooth" });
    });
  }
  if (deptNextBtn && deptGrid) {
    deptNextBtn.addEventListener("click", () => {
      deptGrid.scrollBy({ left: 280, behavior: "smooth" });
    });
  }`;

if (js.includes(oldFilterBadgesClick)) {
  js = js.replace(oldFilterBadgesClick, newFilterBadgesClick);
}

fs.writeFileSync(scriptJsPath, js, 'utf8');
fs.writeFileSync(backupJsPath, js, 'utf8');
console.log('script.js and script_working_backup.js updated with new categories and slider logic!');

// ══════════════════════════════════════════════════════════════════════
// 2. UPDATE index.html — CAROUSEL WRAPPER & 9 DEPARTMENT CARDS
// ══════════════════════════════════════════════════════════════════════
let html = fs.readFileSync(indexHtmlPath, 'utf8');

// Target the old department grid
const oldDeptGrid = `            <!-- 1. Fənn Bölmələri Kartları (Subject Department Selector Cards) -->
            <div class="lecture-dept-grid" id="lecture-dept-grid">
                <button class="lecture-dept-card active" data-filter="all">
                    <div class="lecture-dept-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg>
                    </div>
                    <div class="lecture-dept-body">
                        <span class="lecture-dept-name" data-i18n="filter_all">Hamısı</span>
                        <span class="lecture-dept-meta" id="dept-meta-all">35 Videodərs · Bütün bölmələr</span>
                    </div>
                    <span class="lecture-dept-badge" id="dept-count-all">35</span>
                </button>

                <button class="lecture-dept-card" data-filter="informatika">
                    <div class="lecture-dept-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                    </div>
                    <div class="lecture-dept-body">
                        <span class="lecture-dept-name" data-i18n="filter_informatika">İnformatika</span>
                        <span class="lecture-dept-meta" id="dept-meta-informatika">11 Videodərs · İT və Proqramlaşdırma</span>
                    </div>
                    <span class="lecture-dept-badge" id="dept-count-informatika">11</span>
                </button>

                <button class="lecture-dept-card" data-filter="telekommunikasiya">
                    <div class="lecture-dept-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line></svg>
                    </div>
                    <div class="lecture-dept-body">
                        <span class="lecture-dept-name" data-i18n="filter_telecom">Telekommunikasiya</span>
                        <span class="lecture-dept-meta" id="dept-meta-telekommunikasiya">2 Videodərs · Rabitə Şəbəkələri</span>
                    </div>
                    <span class="lecture-dept-badge" id="dept-count-telekommunikasiya">2</span>
                </button>

                <button class="lecture-dept-card" data-filter="tarix">
                    <div class="lecture-dept-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    </div>
                    <div class="lecture-dept-body">
                        <span class="lecture-dept-name" data-i18n="filter_tarix">Tarix</span>
                        <span class="lecture-dept-meta" id="dept-meta-tarix">8 Videodərs · İctimai Elmlər</span>
                    </div>
                    <span class="lecture-dept-badge" id="dept-count-tarix">8</span>
                </button>

                <button class="lecture-dept-card" data-filter="edebiyyat">
                    <div class="lecture-dept-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                    </div>
                    <div class="lecture-dept-body">
                        <span class="lecture-dept-name" data-i18n="filter_edebiyyat">Ədəbiyyat</span>
                        <span class="lecture-dept-meta" id="dept-meta-edebiyyat">8 Videodərs · Ədəbiyyat və Dil</span>
                    </div>
                    <span class="lecture-dept-badge" id="dept-count-edebiyyat">8</span>
                </button>

                <button class="lecture-dept-card" data-filter="huquq">
                    <div class="lecture-dept-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    </div>
                    <div class="lecture-dept-body">
                        <span class="lecture-dept-name" data-i18n="filter_huquq">Hüquq</span>
                        <span class="lecture-dept-meta" id="dept-meta-huquq">6 Videodərs · Hüquq və Ümumtəhsil</span>
                    </div>
                    <span class="lecture-dept-badge" id="dept-count-huquq">6</span>
                </button>
            </div>`;

const newDeptCarousel = `            <!-- 1. Fənn Bölmələri Sürüşdürülə Bilən Karuseli (Swipeable / Scrollable Subject Track) -->
            <div class="lecture-dept-carousel-wrap">
                <button type="button" class="lecture-dept-nav-btn prev" id="lecture-dept-prev" aria-label="Əvvəlki fənlər" title="Sola çevir">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
                </button>

                <div class="lecture-dept-grid" id="lecture-dept-grid" role="tablist" aria-label="Videodərs fənn bölmələri">
                    <!-- Hamısı -->
                    <button class="lecture-dept-card active" data-filter="all" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_all">Hamısı</span>
                            <span class="lecture-dept-meta">35 Videodərs · Bütün fənlər</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-all">35</span>
                    </button>

                    <!-- İnformatika -->
                    <button class="lecture-dept-card" data-filter="informatika" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_informatika">İnformatika və İKT</span>
                            <span class="lecture-dept-meta">11 Videodərs · Kompüter sistemləri</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-informatika">11</span>
                    </button>

                    <!-- Telekommunikasiya -->
                    <button class="lecture-dept-card" data-filter="telekommunikasiya" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_telecom">Telekommunikasiya</span>
                            <span class="lecture-dept-meta">2 Videodərs · Rabitə şəbəkələri</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-telekommunikasiya">2</span>
                    </button>

                    <!-- Tarix -->
                    <button class="lecture-dept-card" data-filter="tarix" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_tarix">Azərbaycan Tarixi</span>
                            <span class="lecture-dept-meta">8 Videodərs · Tarix və Zəfər</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-tarix">8</span>
                    </button>

                    <!-- Azərbaycan Dili -->
                    <button class="lecture-dept-card" data-filter="az-dili" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_azdili">Azərbaycan Dili</span>
                            <span class="lecture-dept-meta">4 Videodərs · Qrammatika və Nitq</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-az-dili">4</span>
                    </button>

                    <!-- Ədəbiyyat -->
                    <button class="lecture-dept-card" data-filter="edebiyyat" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_edebiyyat">Ədəbiyyat</span>
                            <span class="lecture-dept-meta">4 Videodərs · Bədii ədəbiyyat</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-edebiyyat">4</span>
                    </button>

                    <!-- Hüquq -->
                    <button class="lecture-dept-card" data-filter="huquq" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_huquq">Hüquq və Konstitusiya</span>
                            <span class="lecture-dept-meta">4 Videodərs · Hüquq sistemi</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-huquq">4</span>
                    </button>

                    <!-- Biologiya -->
                    <button class="lecture-dept-card" data-filter="biologiya" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_biologiya">Biologiya</span>
                            <span class="lecture-dept-meta">1 Videodərs · Təbiət elmləri</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-biologiya">1</span>
                    </button>

                    <!-- Çağırışaqədərki Hazırlıq -->
                    <button class="lecture-dept-card" data-filter="gch" role="tab">
                        <div class="lecture-dept-icon">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                        </div>
                        <div class="lecture-dept-body">
                            <span class="lecture-dept-name" data-i18n="filter_gch">Çağırışaqədərki Hazırlıq</span>
                            <span class="lecture-dept-meta">1 Videodərs · Hərbi hazırlıq</span>
                        </div>
                        <span class="lecture-dept-badge" id="dept-count-gch">1</span>
                    </button>
                </div>

                <button type="button" class="lecture-dept-nav-btn next" id="lecture-dept-next" aria-label="Növbəti fənlər" title="Sağa çevir">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                </button>
            </div>`;

if (html.includes(oldDeptGrid)) {
  html = html.replace(oldDeptGrid, newDeptCarousel);
} else {
  console.log('oldDeptGrid not found in index.html');
}

// Update filter badges in index.html (section 3)
const oldFilterBadges = `            <!-- 3. Axtarış və Sürətli Filtr Paneli -->
            <div class="lecture-filter" id="lecture-filter">
                <input type="text" class="library-search" id="lecture-search" placeholder="Videodərs axtar..."
                    data-i18n-placeholder="lecture_search_placeholder" />
                <button class="filter-badge active" data-filter="all" data-i18n="filter_all">
                    Hamısı
                </button>
                <button class="filter-badge" data-filter="informatika" data-i18n="filter_informatika">
                    İnformatika
                </button>
                <button class="filter-badge" data-filter="tarix" data-i18n="filter_tarix">
                    Tarix
                </button>
                <button class="filter-badge" data-filter="edebiyyat" data-i18n="filter_edebiyyat">
                    Ədəbiyyat
                </button>
                <button class="filter-badge" data-filter="huquq" data-i18n="filter_huquq">
                    Hüquq
                </button>
            </div>`;

const newFilterBadges = `            <!-- 3. Axtarış və Sürətli Filtr Paneli (Swipeable Pill Bar) -->
            <div class="lecture-filter" id="lecture-filter">
                <input type="text" class="library-search" id="lecture-search" placeholder="Videodərs axtar..."
                    data-i18n-placeholder="lecture_search_placeholder" />
                <button class="filter-badge active" data-filter="all" data-i18n="filter_all">Hamısı (35)</button>
                <button class="filter-badge" data-filter="informatika" data-i18n="filter_informatika">İnformatika və İKT (11)</button>
                <button class="filter-badge" data-filter="telekommunikasiya" data-i18n="filter_telecom">Telekommunikasiya (2)</button>
                <button class="filter-badge" data-filter="tarix" data-i18n="filter_tarix">Azərbaycan Tarixi (8)</button>
                <button class="filter-badge" data-filter="az-dili" data-i18n="filter_azdili">Azərbaycan Dili (4)</button>
                <button class="filter-badge" data-filter="edebiyyat" data-i18n="filter_edebiyyat">Ədəbiyyat (4)</button>
                <button class="filter-badge" data-filter="huquq" data-i18n="filter_huquq">Hüquq və Konstitusiya (4)</button>
                <button class="filter-badge" data-filter="biologiya" data-i18n="filter_biologiya">Biologiya (1)</button>
                <button class="filter-badge" data-filter="gch" data-i18n="filter_gch">Çağırışaqədərki Hazırlıq (1)</button>
            </div>`;

if (html.includes(oldFilterBadges)) {
  html = html.replace(oldFilterBadges, newFilterBadges);
}

// Update Header Desktop & Mobile dropdowns for Videodərslər
const oldDd = `<div class="nav-dropdown-menu" role="menu" aria-label="Videodərs bölmələri">
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="informatika" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_informatika">İnformatika</span>
                                <span class="nav-dd-sub" data-i18n="dd_lec_info_sub">11 videodərs · İT və Proqramlaşdırma</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="telekommunikasiya" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_telecom">Telekommunikasiya</span>
                                <span class="nav-dd-sub" data-i18n="dd_lec_telecom_sub">2 videodərs · Rabitə Şəbəkələri</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="tarix" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_tarix">Tarix</span>
                                <span class="nav-dd-sub" data-i18n="dd_lec_hist_sub">8 videodərs · İctimai Elmlər</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="edebiyyat" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_edebiyyat">Ədəbiyyat</span>
                                <span class="nav-dd-sub" data-i18n="dd_lec_lit_sub">8 videodərs · Humanitar Fənlər</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="huquq" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_huquq">Hüquq</span>
                                <span class="nav-dd-sub" data-i18n="dd_lec_law_sub">6 videodərs · Hüquq və Ümumtəhsil</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>`;

const newDd = `<div class="nav-dropdown-menu" role="menu" aria-label="Videodərs bölmələri">
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="informatika" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_informatika">İnformatika və İKT</span>
                                <span class="nav-dd-sub">11 videodərs · Kompüter və Şəbəkə</span>
                            </span>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="telekommunikasiya" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_telecom">Telekommunikasiya</span>
                                <span class="nav-dd-sub">2 videodərs · Rabitə Xətləri</span>
                            </span>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="tarix" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_tarix">Azərbaycan Tarixi</span>
                                <span class="nav-dd-sub">8 videodərs · Tarix və Zəfər</span>
                            </span>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="az-dili" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_azdili">Azərbaycan Dili</span>
                                <span class="nav-dd-sub">4 videodərs · Qrammatika və Nitq</span>
                            </span>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="edebiyyat" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_edebiyyat">Ədəbiyyat</span>
                                <span class="nav-dd-sub">4 videodərs · Bədii Ədəbiyyat</span>
                            </span>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="huquq" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_huquq">Hüquq və Konstitusiya</span>
                                <span class="nav-dd-sub">4 videodərs · Hüquq Sistemi</span>
                            </span>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="biologiya" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_biologiya">Biologiya</span>
                                <span class="nav-dd-sub">1 videodərs · Təbiət Elmləri</span>
                            </span>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" data-lecture-cat="gch" role="menuitem">
                            <span class="nav-dd-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="filter_gch">Çağırışaqədərki Hazırlıq</span>
                                <span class="nav-dd-sub">1 videodərs · Hərbi Vətənpərvərlik</span>
                            </span>
                        </a>
                    </div>`;

if (html.includes(oldDd)) {
  html = html.replace(oldDd, newDd);
}

// Bump cache version in index.html to v=20261105_10
html = html.replace(/20261105_09/g, '20261105_10');

fs.writeFileSync(indexHtmlPath, html, 'utf8');
console.log('index.html updated with carousel wrapper, 9 department cards, and dropdown!');

// ══════════════════════════════════════════════════════════════════════
// 3. UPDATE style.css — SWIPEABLE TRACK & ARROW BUTTON STYLES
// ══════════════════════════════════════════════════════════════════════
let css = fs.readFileSync(styleCssPath, 'utf8');

const sliderCss = `
/* ═══════════════════════════════════════════════════════════════════════
   VIDEODƏRSLƏR FƏNN KARUSELİ VƏ SÜRÜŞDÜRÜLƏ BİLƏN XRONOLOJİ ZOLAĞI
   ═══════════════════════════════════════════════════════════════════════ */
.lecture-dept-carousel-wrap {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 32px;
}

.lecture-dept-grid {
  display: flex !important;
  flex-direction: row !important;
  overflow-x: auto !important;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  gap: 16px;
  padding: 10px 4px 18px !important;
  margin-bottom: 0 !important;
  scrollbar-width: thin;
  scrollbar-color: var(--gold) rgba(6, 19, 38, 0.4);
  flex: 1;
}

.lecture-dept-grid::-webkit-scrollbar {
  height: 6px;
}

.lecture-dept-grid::-webkit-scrollbar-track {
  background: rgba(6, 19, 38, 0.6);
  border-radius: 999px;
}

.lecture-dept-grid::-webkit-scrollbar-thumb {
  background: linear-gradient(90deg, var(--gold), #b8934a);
  border-radius: 999px;
}

.lecture-dept-card {
  min-width: 255px !important;
  max-width: 280px !important;
  flex: 0 0 auto !important;
  cursor: pointer;
  border-radius: 20px !important;
  user-select: none;
  background: linear-gradient(145deg, rgba(10, 32, 60, 0.9), rgba(6, 19, 38, 0.98)) !important;
  border: 1.5px solid rgba(207, 169, 94, 0.3) !important;
  transition: all 0.28s ease !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
}

.lecture-dept-card:hover {
  transform: translateY(-4px) !important;
  border-color: var(--gold) !important;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(207, 169, 94, 0.25) !important;
}

.lecture-dept-card.active {
  border-color: var(--gold) !important;
  background: linear-gradient(145deg, rgba(207, 169, 94, 0.22), rgba(6, 19, 38, 0.98)) !important;
  box-shadow: 0 10px 30px rgba(207, 169, 94, 0.35) !important;
}

.lecture-dept-nav-btn {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: rgba(10, 34, 64, 0.95);
  border: 1.5px solid var(--gold);
  color: var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: all 0.25s ease;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
  z-index: 5;
}

.lecture-dept-nav-btn:hover {
  background: var(--gold);
  color: #061326;
  transform: scale(1.1);
  box-shadow: 0 8px 25px rgba(207, 169, 94, 0.5);
}

.lecture-filter {
  display: flex !important;
  align-items: center;
  gap: 10px;
  overflow-x: auto !important;
  padding: 4px 2px 14px;
  scrollbar-width: none;
  margin-bottom: 24px;
  white-space: nowrap;
}

.lecture-filter::-webkit-scrollbar {
  display: none;
}

.lecture-filter .filter-badge {
  flex-shrink: 0;
  white-space: nowrap;
}
`;

if (!css.includes('.lecture-dept-carousel-wrap')) {
  css += '\n' + sliderCss;
  fs.writeFileSync(styleCssPath, css, 'utf8');
  console.log('style.css updated with carousel slider styles!');
} else {
  console.log('style.css already has carousel styles.');
}

