import os, sys, re, html

base_dir = "/Users/konul/Documents/esas2 copy 2"

# 1. READ ORIGINAL FILES
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html_src = f.read()

with open(os.path.join(base_dir, "style.css"), "r", encoding="utf-8") as f:
    css_src = f.read()

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

print("Original files loaded. Lengths:", len(html_src), len(css_src), len(js_src))

# 2. UPDATE INDEX.HTML
# 2.1 Add Desktop nav dropdown item
target_dd_majors = '<a href="#structure" class="nav-dropdown-item" data-struct-cat="majors" role="menuitem">'
replacement_dd_campus = '''<a href="#campus-navigator" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><line x1="9" y1="6" x2="9" y2="6.01"></line><line x1="15" y1="6" x2="15" y2="6.01"></line><line x1="9" y1="10" x2="9" y2="10.01"></line><line x1="15" y1="10" x2="15" y2="10.01"></line><line x1="9" y1="14" x2="9" y2="14.01"></line><line x1="15" y1="14" x2="15" y2="14.01"></line><line x1="9" y1="18" x2="15" y2="18"></line></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_campus">Kampus & Otaqlar</span>
                                <span class="nav-dd-sub" data-i18n="nav_campus_sub">5 mərtəbəli bina naviqasiyası</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#structure" class="nav-dropdown-item" data-struct-cat="majors" role="menuitem">'''

if target_dd_majors in html_src and 'href="#campus-navigator"' not in html_src:
    html_src = html_src.replace(target_dd_majors, replacement_dd_campus, 1)
    print("Added desktop dropdown nav item.")

# 2.2 Add Desktop top-level nav link
target_nav_lib = '<a href="#library" class="nav-link" data-i18n="nav_library">Kitabxana</a>'
replacement_nav_campus = '<a href="#campus-navigator" class="nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>\n                <a href="#library" class="nav-link" data-i18n="nav_library">Kitabxana</a>'

if target_nav_lib in html_src:
    html_src = html_src.replace(target_nav_lib, replacement_nav_campus, 1)
    print("Added desktop top-level nav link.")

# 2.3 Add Mobile nav link
target_mob_majors = '<a href="#structure" class="mobile-nav-sublink" data-struct-cat="majors" data-i18n="cat_majors">İxtisaslar</a>'
replacement_mob_campus = '''<a href="#structure" class="mobile-nav-sublink" data-struct-cat="majors" data-i18n="cat_majors">İxtisaslar</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-i18n="nav_campus">Kampus & Otaqlar</a>'''

if target_mob_majors in html_src:
    html_src = html_src.replace(target_mob_majors, replacement_mob_campus, 1)
    print("Added mobile dropdown sublink.")

target_mob_lib = '<a href="#library" class="mobile-nav-link" data-i18n="nav_library">Kitabxana</a>'
replacement_mob_main = '<a href="#campus-navigator" class="mobile-nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>\n            <a href="#library" class="mobile-nav-link" data-i18n="nav_library">Kitabxana</a>'

if target_mob_lib in html_src:
    html_src = html_src.replace(target_mob_lib, replacement_mob_main, 1)
    print("Added mobile top-level nav link.")

# 2.4 Insert #campus-navigator section right before <!-- ═══════════════ PDF LIBRARY ═══════════════ -->
campus_section_html = '''    <!-- ═══════════════ INTERACTIVE DIGITAL CAMPUS NAVIGATOR (OTAQLAR.docx) ═══════════════ -->
    <section class="section campus-navigator-section" id="campus-navigator">
        <div class="section-inner reveal">
            <!-- Header Badge & Title -->
            <div class="campus-header-center">
                <span class="section-badge" data-i18n="campus_badge">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    Kampus İnfrastrukturu & Bələdçi
                </span>
                <h2 class="section-title" data-i18n="campus_title">Tədris Korpusu və Ağıllı Otaq Naviqatoru</h2>
                <p class="section-desc" data-i18n="campus_desc">
                    5 mərtəbəli əsas tədris korpusumuzun rəqəmsal bələdçisi. Müasir laboratoriyalar, auditoriyalar, inzibati şöbələr və tələbə məkanları üzrə ani axtarış və interaktiv mərtəbə naviqatoru.
                </p>
            </div>

            <!-- Stats Bar -->
            <div class="campus-stats-bar">
                <div class="campus-stat-item">
                    <div class="campus-stat-icon">🏢</div>
                    <div class="campus-stat-info">
                        <span class="campus-stat-val">5 Mərtəbə</span>
                        <span class="campus-stat-label">Əsas Tədris Korpusu</span>
                    </div>
                </div>
                <div class="campus-stat-item">
                    <div class="campus-stat-icon">🚪</div>
                    <div class="campus-stat-info">
                        <span class="campus-stat-val">80+ Auditoriya</span>
                        <span class="campus-stat-label">Tədris və İnzibati Məkan</span>
                    </div>
                </div>
                <div class="campus-stat-item">
                    <div class="campus-stat-icon">🔬</div>
                    <div class="campus-stat-info">
                        <span class="campus-stat-val">7 Laboratoriya</span>
                        <span class="campus-stat-label">Kimya, Fizika, Rabitə, İKT</span>
                    </div>
                </div>
                <div class="campus-stat-item">
                    <div class="campus-stat-icon">📚</div>
                    <div class="campus-stat-info">
                        <span class="campus-stat-val">206-cı Otaq</span>
                        <span class="campus-stat-label">22 000+ Kitab Fondu & Oxu Zalı</span>
                    </div>
                </div>
            </div>

            <!-- Floor Selector Switcher -->
            <div class="campus-floors-wrapper">
                <div class="campus-floors-nav" role="tablist" aria-label="Mərtəbə seçimi">
                    <button type="button" class="campus-floor-btn active" data-floor="1" role="tab" aria-selected="true">
                        <span class="floor-num-badge">I</span>
                        <span class="floor-title-text">1-ci Mərtəbə</span>
                        <span class="floor-meta-count">12 otaq · İdman & Lab</span>
                    </button>
                    <button type="button" class="campus-floor-btn" data-floor="2" role="tab" aria-selected="false">
                        <span class="floor-num-badge">II</span>
                        <span class="floor-title-text">2-ci Mərtəbə</span>
                        <span class="floor-meta-count">11 otaq · Rəhbərlik & Kitabxana</span>
                    </button>
                    <button type="button" class="campus-floor-btn" data-floor="3" role="tab" aria-selected="false">
                        <span class="floor-num-badge">III</span>
                        <span class="floor-title-text">3-cü Mərtəbə</span>
                        <span class="floor-meta-count">16 otaq · Fizika Lab & Tədris</span>
                    </button>
                    <button type="button" class="campus-floor-btn" data-floor="4" role="tab" aria-selected="false">
                        <span class="floor-num-badge">IV</span>
                        <span class="floor-title-text">4-cü Mərtəbə</span>
                        <span class="floor-meta-count">17 otaq · İKT & Poçt Lab</span>
                    </button>
                    <button type="button" class="campus-floor-btn" data-floor="5" role="tab" aria-selected="false">
                        <span class="floor-num-badge">V</span>
                        <span class="floor-title-text">5-ci Mərtəbə</span>
                        <span class="floor-meta-count">18 otaq · Kompüter & Keyfiyyət</span>
                    </button>
                    <button type="button" class="campus-floor-btn" data-floor="all" role="tab" aria-selected="false">
                        <span class="floor-num-badge">Bütün</span>
                        <span class="floor-title-text">Bütün Mərtəbələr</span>
                        <span class="floor-meta-count">80+ otaq</span>
                    </button>
                </div>
            </div>

            <!-- Floor Architectural Summary Banner -->
            <div class="campus-floor-banner" id="campus-floor-banner">
                <div class="cfb-header">
                    <div class="cfb-title-wrap">
                        <span class="cfb-floor-icon">🏢</span>
                        <div>
                            <h3 class="cfb-title">I MƏRTƏBƏ — İdman Kompleksi, Kimya & Rabitə Laboratoriyaları</h3>
                            <p class="cfb-desc">Kollecin 1-ci mərtəbəsində tələbələrin fiziki hazırlığı üçün idman zalı, 2 kimya laboratoriyası, telekommunikasiya laboratoriyası və inzibati şöbələr yerləşir.</p>
                        </div>
                    </div>
                    <span class="cfb-badge-count">12 Əsas Otaq və Məkan</span>
                </div>
                <div class="cfb-wings">
                    <span class="cfb-wing-chip">⬅️ <strong>Qərb Qanadı:</strong> 107 (Qiyabi), 106A (Hərbi), 106 (Kimya-1), 107A (Telekom), 103 (Kimya-2)</span>
                    <span class="cfb-wing-chip">🏛️ <strong>Mərkəzi:</strong> Kadrlar şöbəsi, Kompüter laboratoriyası</span>
                    <span class="cfb-wing-chip">➡️ <strong>Şərq Qanadı:</strong> 113 (Mühasibat - 2 otaq), 114 (Təsərrüfat), 115 (Təcrübə), 116 (Tərbiyə)</span>
                    <span class="cfb-wing-chip">⚽ <strong>İdman:</strong> İdman zalı (geyinmə otağı ilə)</span>
                </div>
            </div>

            <!-- Controls Bar: Search & Category Chips -->
            <div class="campus-controls-bar">
                <div class="campus-search-box">
                    <svg class="campus-search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <input type="text" id="campus-search-input" placeholder="Otaq nömrəsi və ya ad ilə axtarın (məs: 206, Kimya, Fizika, Direktor, Poçt, 107)..." aria-label="Otaq axtarışı">
                    <button type="button" id="campus-search-clear" class="campus-search-clear-btn" aria-label="Axtarışı təmizlə" style="display:none;">&times;</button>
                </div>

                <div class="campus-category-chips" id="campus-cat-filters">
                    <button type="button" class="campus-chip active" data-cat="all">Hamısı</button>
                    <button type="button" class="campus-chip" data-cat="lab">🔬 Laboratoriyalar</button>
                    <button type="button" class="campus-chip" data-cat="it">💻 Kompüter və İKT</button>
                    <button type="button" class="campus-chip" data-cat="admin">🏛️ Rəhbərlik & İnzibati</button>
                    <button type="button" class="campus-chip" data-cat="library">📚 Kitabxana & Oxu Zalı</button>
                    <button type="button" class="campus-chip" data-cat="sport">⚽ İdman & Hərbi</button>
                    <button type="button" class="campus-chip" data-cat="classroom">🎓 Auditoriyalar</button>
                </div>
            </div>

            <!-- Filter Status -->
            <div class="campus-filter-status" id="campus-filter-status">
                <span id="campus-rooms-count-text">Göstərilən otaqlar: <strong>12</strong></span>
                <span class="campus-filter-hint">Otaq kartına basaraq ətraflı bələdçi məlumatını əldə edin</span>
            </div>

            <!-- Rooms Grid -->
            <div class="campus-rooms-grid" id="campus-rooms-grid">
                <!-- Dynamically populated and reactive -->
            </div>
        </div>
    </section>

'''

target_lib_section = '    <!-- ═══════════════ PDF LIBRARY ═══════════════ -->'
if target_lib_section in html_src and 'id="campus-navigator"' not in html_src:
    html_src = html_src.replace(target_lib_section, campus_section_html + target_lib_section, 1)
    print("Added #campus-navigator section before #library.")

# 2.5 Insert #campus-room-modal markup before </body>
campus_modal_html = '''    <!-- ═══ CAMPUS ROOM DETAIL & GUIDE MODAL ═══ -->
    <div class="campus-modal-backdrop" id="campus-room-modal" role="dialog" aria-modal="true" aria-hidden="true">
        <div class="campus-modal-card">
            <div class="campus-modal-header">
                <div class="campus-modal-tags">
                    <span class="campus-modal-floor-badge" id="crm-floor-badge">I Mərtəbə</span>
                    <span class="campus-modal-room-badge" id="crm-room-badge">№ 107</span>
                    <span class="campus-modal-cat-badge" id="crm-cat-badge">Laboratoriya</span>
                </div>
                <button type="button" class="campus-modal-close" id="crm-close-btn" aria-label="Bağla">&times;</button>
            </div>
            <div class="campus-modal-body">
                <div class="campus-modal-icon-box" id="crm-icon-box">🔬</div>
                <h3 class="campus-modal-title" id="crm-title">Otaq Adı</h3>
                <p class="campus-modal-desc" id="crm-desc">Təsvir</p>

                <div class="campus-modal-features-wrap">
                    <h4 class="campus-modal-subtitle">Xüsusiyyətlər və Təchizat:</h4>
                    <div class="campus-modal-features" id="crm-features"></div>
                </div>

                <div class="campus-modal-navguide">
                    <div class="campus-navguide-item">
                        <span class="cng-icon">📍</span>
                        <div class="cng-text">
                            <strong>Məkan:</strong> <span id="crm-loc">1-ci Mərtəbə, Şərq Qanadı</span>
                        </div>
                    </div>
                    <div class="campus-navguide-item">
                        <span class="cng-icon">🧭</span>
                        <div class="cng-text">
                            <strong>İstiqamət:</strong> <span id="crm-route">Mərkəzi girişdən sağa dönün</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="campus-modal-footer" id="crm-footer">
                <button type="button" class="btn btn-secondary" id="crm-footer-close">Bağla</button>
            </div>
        </div>
    </div>
'''

if 'id="campus-room-modal"' not in html_src:
    html_src = html_src.replace('</body>', campus_modal_html + '\n</body>', 1)
    print("Added #campus-room-modal before </body>.")

# 2.6 Bump Cache Version to v=20261106_31
html_src = re.sub(r'style\.css\?v=[a-zA-Z0-9_]+', 'style.css?v=20261106_31', html_src)
html_src = re.sub(r'script\.js\?v=[a-zA-Z0-9_]+', 'script.js?v=20261106_31', html_src)
print("Updated cache version to v=20261106_31.")

# Save index.html
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_src)
print("index.html saved successfully.")

# 3. UPDATE STYLE.CSS
with open(os.path.join(base_dir, "scratch/campus_styles.css"), "r", encoding="utf-8") as f:
    campus_css = f.read()

if "CAMPUS & ROOM NAVIGATOR (OTAQLAR.docx) STYLES" not in css_src:
    css_src += "\n\n" + campus_css
    with open(os.path.join(base_dir, "style.css"), "w", encoding="utf-8") as f:
        f.write(css_src)
    print("style.css updated with campus styles.")
else:
    print("style.css already contains campus styles.")

print("HTML & CSS steps finished.")
