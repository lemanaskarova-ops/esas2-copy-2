const fs = require('fs');
const path = require('path');

const rootDir = '/Users/konul/Documents/esas2 copy 2';
const indexHtmlPath = path.join(rootDir, 'index.html');
const styleCssPath = path.join(rootDir, 'style.css');
const scriptJsPath = path.join(rootDir, 'script.js');
const backupJsPath = path.join(rootDir, 'scratch/script_working_backup.js');

// 1. UPDATE index.html
let html = fs.readFileSync(indexHtmlPath, 'utf8');

// A. Add navigation link to desktop nav
const desktopNavTarget = '<a href="#gallery" class="nav-link" data-i18n="nav_gallery">Qalereya</a>';
const desktopNavReplacement = '<a href="#honor-students" class="nav-link" data-i18n="nav_honors">Fəxri Tələbələr</a>\n                <a href="#gallery" class="nav-link" data-i18n="nav_gallery">Qalereya</a>';
if (html.includes(desktopNavTarget) && !html.includes('href="#honor-students"')) {
  html = html.replace(desktopNavTarget, desktopNavReplacement);
}

// B. Add navigation link to mobile nav
const mobileNavTarget = '<a href="#gallery" class="mobile-nav-link" data-i18n="nav_gallery">Qalereya</a>';
const mobileNavReplacement = '<a href="#honor-students" class="mobile-nav-link" data-i18n="nav_honors">Fəxri Tələbələr</a>\n            <a href="#gallery" class="mobile-nav-link" data-i18n="nav_gallery">Qalereya</a>';
if (html.includes(mobileNavTarget) && !html.includes('class="mobile-nav-link" data-i18n="nav_honors"')) {
  html = html.replace(mobileNavTarget, mobileNavReplacement);
}

// C. Insert Honor Students Section inside #graduates
const gradInnerEnd = `                <a href="https://www.instagram.com/reel/Dac8pZFqLfE/" target="_blank" rel="noopener" class="grad-cta">
                    <span data-i18n="grad_cta">Instagram-da izlə</span>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
            </div>
        </div>
    </section>`;

const honorSectionHtml = `                <a href="https://www.instagram.com/reel/Dac8pZFqLfE/" target="_blank" rel="noopener" class="grad-cta">
                    <span data-i18n="grad_cta">Instagram-da izlə</span>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
            </div>
        </div>

        <!-- ═══════════════ FƏXRİ TƏLƏBƏLƏR & ŞƏRƏF LÖVHƏSİ (HALL OF FAME) ═══════════════ -->
        <div class="grad-honors-wrap reveal" id="honor-students">
            <div class="grad-honors-header">
                <div class="grad-honors-badge-row">
                    <span class="grad-honors-kicker">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
                            <circle cx="12" cy="8" r="7"></circle>
                            <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                        </svg>
                        <span data-i18n="honors_kicker">ŞƏRƏF LÖVHƏSİ · FƏXRİ TƏLƏBƏLƏRİMİZ</span>
                    </span>
                    <span class="grad-honors-sub-badge">
                        <span class="sub-badge-star">✦</span>
                        <span>Qlobal Nailiyyətlər & Beynəlxalq Təmsilçilik</span>
                    </span>
                </div>
                <h3 class="grad-honors-title" data-i18n="honors_title">Beynəlxalq Arenada Kollecimizin İmzası</h3>
                <p class="grad-honors-desc" data-i18n="honors_desc">
                    İnformasiya texnologiyaları, kibertəhlükəsizlik və robototexnika sahələrində beynəlxalq çempionluqlar qazanan, Azərbaycan bayrağını ABŞ, Yaponiya və Avropada dalğalandıran fəxri tələbələrimiz.
                </p>

                <!-- Filter Tabs -->
                <div class="grad-honors-tabs" role="tablist" aria-label="Fəxri tələbə kateqoriyaları">
                    <button type="button" class="honor-tab-btn active" data-honor-filter="all" role="tab" aria-selected="true">
                        <span class="tab-emoji">🌟</span>
                        <span>Hamısı</span>
                        <span class="honor-tab-count" id="honor-count-all">1</span>
                    </button>
                    <button type="button" class="honor-tab-btn" data-honor-filter="it-robotics" role="tab" aria-selected="false">
                        <span class="tab-emoji">🤖</span>
                        <span>İKT & Robototexnika</span>
                        <span class="honor-tab-count">1</span>
                    </button>
                    <button type="button" class="honor-tab-btn" data-honor-filter="international" role="tab" aria-selected="false">
                        <span class="tab-emoji">🌍</span>
                        <span>Beynəlxalq Çempionatlar</span>
                        <span class="honor-tab-count">1</span>
                    </button>
                    <button type="button" class="honor-tab-btn" data-honor-filter="youth" role="tab" aria-selected="false">
                        <span class="tab-emoji">🎖️</span>
                        <span>İlin Gənci & Sosial İnklüzivlik</span>
                        <span class="honor-tab-count">1</span>
                    </button>
                </div>
            </div>

            <!-- Fəxri Tələbələr Vitrini (Dinamik render olunur) -->
            <div class="grad-honors-grid" id="honor-students-grid">
                <!-- Javascript will render the student cards here -->
            </div>
        </div>
    </section>`;

if (html.includes(gradInnerEnd)) {
  html = html.replace(gradInnerEnd, honorSectionHtml);
} else {
  console.error('Could not find gradInnerEnd in index.html');
}

// D. Add Modal Markup before script tag
const modalMarkup = `
    <!-- ═══ FƏXRİ TƏLƏBƏ ƏTRAFLI DOSYE VƏ NAİLİYYƏT MODALI ═══ -->
    <div class="honor-modal-overlay" id="honor-student-modal" role="dialog" aria-modal="true" aria-hidden="true">
        <div class="honor-modal-container">
            <button class="honor-modal-close" id="honor-modal-close" aria-label="Bağla">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
            </button>
            <div class="honor-modal-body" id="honor-modal-body">
                <!-- Javascript tərəfindən dinamik qurulur -->
            </div>
        </div>
    </div>
`;

if (!html.includes('id="honor-student-modal"')) {
  const scriptTagTarget = '<script src="script.js?v=';
  html = html.replace(scriptTagTarget, modalMarkup + '\n    ' + scriptTagTarget);
}

// E. Bump cache version to v=20261105_01
html = html.replace(/style\.css\?v=[^"']+/g, 'style.css?v=20261105_01');
html = html.replace(/script\.js\?v=[^"']+/g, 'script.js?v=20261105_01');

fs.writeFileSync(indexHtmlPath, html, 'utf8');
console.log('index.html updated successfully!');

