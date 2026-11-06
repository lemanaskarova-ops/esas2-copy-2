# -*- coding: utf-8 -*-
import os, re

base_dir = '/Users/konul/Documents/esas2 copy 2'
html_path = os.path.join(base_dir, 'index.html')
js_path = os.path.join(base_dir, 'script.js')
backup_js_path = os.path.join(base_dir, 'scratch/script_working_backup.js')

# 1. NEW i18n KEYS
NEW_NAV_KEYS_AZ = {
    "nav_college": "Kollecimiz",
    "nav_about_sub": "Kollecin yaranma tarixi və missiyası",
    "nav_structure_sub": "İdarə heyəti, şöbələr və FBK-lar",
    "nav_honors_sub": "Beynəlxalq çempionlar və şərəf lövhəsi",
    "nav_academics": "Tədris & Elm",
    "nav_lectures_sub": "23 rəsmi videodərs və multimedia arxivi",
    "nav_library_sub": "44+ dərslik, fond və daxili oxu zalı",
    "nav_science_sub": "Fakültənin beynəlxalq və yerli elmi məqalələri",
    "nav_media": "Media & Həyat",
    "nav_news_sub": "Rəsmi elanlar və kollec tədbirləri",
    "nav_qarabag": "Qarabağ Zəfər Salnaməsi",
    "nav_qarabag_sub": "Ağdam, Xankəndi və Şuşa səfəri xronikası",
    "nav_gallery_sub": "İmtahan, tədbir və laboratoriya kadrları",
    "nav_certificates_sub": "Respublika spartakiadası və rəsmi diplomlar"
}

NEW_NAV_KEYS_EN = {
    "nav_college": "Our College",
    "nav_about_sub": "College history and mission",
    "nav_structure_sub": "Leadership, departments & commissions",
    "nav_honors_sub": "International champions & honor roll",
    "nav_academics": "Academics & Science",
    "nav_lectures_sub": "23 video lectures & media archive",
    "nav_library_sub": "44+ textbooks, collection & reading room",
    "nav_science_sub": "Faculty international and local research",
    "nav_media": "Media & Campus Life",
    "nav_news_sub": "Official announcements & college events",
    "nav_qarabag": "Karabakh Victory Chronicle",
    "nav_qarabag_sub": "Chronicle of visit to Aghdam, Khankendi & Shusha",
    "nav_gallery_sub": "Exam, event and lab photo footage",
    "nav_certificates_sub": "National spartakiad and official diplomas"
}

NEW_NAV_KEYS_RU = {
    "nav_college": "Наш Колледж",
    "nav_about_sub": "История создания и миссия колледжа",
    "nav_structure_sub": "Руководство, отделы и ПЦК",
    "nav_honors_sub": "Международные чемпионы и доска почета",
    "nav_academics": "Учеба и Наука",
    "nav_lectures_sub": "23 видеоурока и медиа-архив",
    "nav_library_sub": "44+ учебника, фонд и читальный зал",
    "nav_science_sub": "Международные и местные научные статьи",
    "nav_media": "Медиа и Жизнь",
    "nav_news_sub": "Официальные объявления и события",
    "nav_qarabag": "Летопись Карабахской Победы",
    "nav_qarabag_sub": "Хроника поездки в Агдам, Ханкенди и Шушу",
    "nav_gallery_sub": "Кадры с экзаменов, событий и лабораторий",
    "nav_certificates_sub": "Республиканская спартакиада и дипломы"
}

# Update script.js dictionaries
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

def inject_keys(lang, d, content):
    pattern = r'(' + lang + r':\s*\{[\s\S]*?)(\n  \},|\n  \})'
    m = re.search(pattern, content)
    if not m: return content
    lines = []
    for k, v in d.items():
        if f'{k}:' not in content[m.start():m.end()]:
            lines.append(f'    {k}: "{v}",')
    if not lines: return content
    block = '\n' + '\n'.join(lines)
    return content[:m.start()] + m.group(1) + block + m.group(2) + content[m.end():]

js = inject_keys('az', NEW_NAV_KEYS_AZ, js)
js = inject_keys('en', NEW_NAV_KEYS_EN, js)
js = inject_keys('ru', NEW_NAV_KEYS_RU, js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
with open(backup_js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print('Updated script.js with new navigation keys.')

# 2. CONSTRUCT NEW DESKTOP NAV HTML
DESKTOP_NAV_HTML = """<nav class="header-nav" id="desktop-nav" aria-label="Əsas naviqasiya">
                <!-- 1. Ana Səhifə -->
                <a href="#hero" class="nav-link" data-i18n="nav_home">Ana Səhifə</a>

                <!-- 2. Kollecimiz Dropdown -->
                <div class="nav-dropdown">
                    <a href="#about" class="nav-link nav-dropdown-trigger" aria-haspopup="true">
                        <span data-i18n="nav_college">Kollecimiz</span>
                        <svg class="nav-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu" role="menu" aria-label="Kollec bölmələri">
                        <a href="#about" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">🏛️</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_about">Haqqımızda</span>
                                <span class="nav-dd-sub" data-i18n="nav_about_sub">Kollecin yaranma tarixi və missiyası</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#structure" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">👥</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_structure">Rəhbərlik & Struktur</span>
                                <span class="nav-dd-sub" data-i18n="nav_structure_sub">İdarə heyəti, şöbələr və FBK-lar</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#honor-students" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">🌟</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_honors">Fəxri Tələbələr</span>
                                <span class="nav-dd-sub" data-i18n="nav_honors_sub">Beynəlxalq çempionlar və şərəf lövhəsi</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>
                </div>

                <!-- 3. Tədris & Elm Dropdown -->
                <div class="nav-dropdown">
                    <a href="#lectures" class="nav-link nav-dropdown-trigger" aria-haspopup="true">
                        <span data-i18n="nav_academics">Tədris & Elm</span>
                        <svg class="nav-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu" role="menu" aria-label="Tədris və elm bölmələri">
                        <a href="#structure" class="nav-dropdown-item" data-struct-cat="majors" role="menuitem">
                            <span class="nav-dd-icon">🎓</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="cat_majors">İxtisaslar</span>
                                <span class="nav-dd-sub" data-i18n="cat_majors_sub">Tədris olunan bütün sahələr</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#lectures" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">🎬</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_lectures">Videodərslər Studiyası</span>
                                <span class="nav-dd-sub" data-i18n="nav_lectures_sub">23 rəsmi videodərs və multimedia arxivi</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#library" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">📚</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_library">Elektron Kitabxana</span>
                                <span class="nav-dd-sub" data-i18n="nav_library_sub">44+ dərslik, fond və daxili oxu zalı</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#science" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">🔬</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_science">Elm və Nəşrlər</span>
                                <span class="nav-dd-sub" data-i18n="nav_science_sub">Fakültənin beynəlxalq və yerli elmi məqalələri</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>
                </div>

                <!-- 4. Kampus & Otaqlar Dropdown -->
                <div class="nav-dropdown">
                    <a href="#campus-navigator" class="nav-link nav-dropdown-trigger" aria-haspopup="true">
                        <span data-i18n="nav_campus">Kampus & Otaqlar</span>
                        <svg class="nav-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu" role="menu" aria-label="Mərtəbələr və otaqlar">
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="1" role="menuitem">
                            <span class="nav-dd-icon">🏢</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="campus_nav_floor_1">I Mərtəbə</span>
                                <span class="nav-dd-sub" data-i18n="campus_nav_floor_1_sub">İdman kompleksi, Kimya & Telekom</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="2" role="menuitem">
                            <span class="nav-dd-icon">🏛️</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="campus_nav_floor_2">II Mərtəbə</span>
                                <span class="nav-dd-sub" data-i18n="campus_nav_floor_2_sub">Rəhbərlik, Kitabxana & Optika</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="3" role="menuitem">
                            <span class="nav-dd-icon">🎓</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="campus_nav_floor_3">III Mərtəbə</span>
                                <span class="nav-dd-sub" data-i18n="campus_nav_floor_3_sub">Tədris şöbələri, Nəqliyyat & Poçt</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="4" role="menuitem">
                            <span class="nav-dd-icon">💻</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="campus_nav_floor_4">IV Mərtəbə</span>
                                <span class="nav-dd-sub" data-i18n="campus_nav_floor_4_sub">Kompüter Mərkəzi & İKT Laboratoriyaları</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="5" role="menuitem">
                            <span class="nav-dd-icon">📡</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="campus_nav_floor_5">V Mərtəbə</span>
                                <span class="nav-dd-sub" data-i18n="campus_nav_floor_5_sub">Texniki fənlər, Şəbəkə & İmtahan</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="all" role="menuitem">
                            <span class="nav-dd-icon">🗺️</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="campus_nav_all">Bütün Mərtəbələr</span>
                                <span class="nav-dd-sub" data-i18n="campus_nav_all_sub">39 otağın tam interaktiv xəritəsi</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>
                </div>

                <!-- 5. Media & Həyat Dropdown -->
                <div class="nav-dropdown">
                    <a href="#news" class="nav-link nav-dropdown-trigger" aria-haspopup="true">
                        <span data-i18n="nav_media">Media & Həyat</span>
                        <svg class="nav-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu" role="menu" aria-label="Media və tələbə həyatı bölmələri">
                        <a href="#news" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">📰</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_news">Son Xəbərlər</span>
                                <span class="nav-dd-sub" data-i18n="nav_news_sub">Rəsmi elanlar və kollec tədbirləri</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#qarabag" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">🇦🇿</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_qarabag">Qarabağ Zəfər Salnaməsi</span>
                                <span class="nav-dd-sub" data-i18n="nav_qarabag_sub">Ağdam, Xankəndi və Şuşa səfəri xronikası</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#gallery" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">📸</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_gallery">Foto & Video Qalereya</span>
                                <span class="nav-dd-sub" data-i18n="nav_gallery_sub">İmtahan, tədbir və laboratoriya kadrları</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#certificates" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">🏆</span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_certificates">Nailiyyətlər & Kuboklar</span>
                                <span class="nav-dd-sub" data-i18n="nav_certificates_sub">Respublika spartakiadası və rəsmi diplomlar</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>
                </div>

                <!-- 6. Əlaqə -->
                <a href="#contact" class="nav-link" data-i18n="nav_contact">Əlaqə</a>
            </nav>"""

# 3. CONSTRUCT NEW MOBILE NAV HTML
MOBILE_NAV_HTML = """<div class="mobile-nav-drawer" id="mobile-nav">
        <nav class="mobile-nav-inner">
            <a href="#hero" class="mobile-nav-link" data-i18n="nav_home">Ana Səhifə</a>

            <!-- 1. Kollecimiz Group -->
            <div class="mobile-nav-group">
                <a href="#about" class="mobile-nav-link" data-i18n="nav_college">Kollecimiz</a>
                <div class="mobile-nav-sub">
                    <a href="#about" class="mobile-nav-sublink" data-i18n="nav_about">Haqqımızda</a>
                    <a href="#structure" class="mobile-nav-sublink" data-i18n="nav_structure">Rəhbərlik & Struktur</a>
                    <a href="#honor-students" class="mobile-nav-sublink" data-i18n="nav_honors">Fəxri Tələbələr</a>
                </div>
            </div>

            <!-- 2. Tədris & Elm Group -->
            <div class="mobile-nav-group">
                <a href="#lectures" class="mobile-nav-link" data-i18n="nav_academics">Tədris & Elm</a>
                <div class="mobile-nav-sub">
                    <a href="#structure" class="mobile-nav-sublink" data-struct-cat="majors" data-i18n="cat_majors">İxtisaslar</a>
                    <a href="#lectures" class="mobile-nav-sublink" data-i18n="nav_lectures">Videodərslər Studiyası</a>
                    <a href="#library" class="mobile-nav-sublink" data-i18n="nav_library">Elektron Kitabxana</a>
                    <a href="#science" class="mobile-nav-sublink" data-i18n="nav_science">Elm və Nəşrlər</a>
                </div>
            </div>

            <!-- 3. Kampus & Otaqlar Group -->
            <div class="mobile-nav-group">
                <a href="#campus-navigator" class="mobile-nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>
                <div class="mobile-nav-sub">
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="1" data-i18n="campus_nav_floor_1">I Mərtəbə</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="2" data-i18n="campus_nav_floor_2">II Mərtəbə</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="3" data-i18n="campus_nav_floor_3">III Mərtəbə</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="4" data-i18n="campus_nav_floor_4">IV Mərtəbə</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="5" data-i18n="campus_nav_floor_5">V Mərtəbə</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="all" data-i18n="campus_nav_all">Bütün Mərtəbələr</a>
                </div>
            </div>

            <!-- 4. Media & Həyat Group -->
            <div class="mobile-nav-group">
                <a href="#news" class="mobile-nav-link" data-i18n="nav_media">Media & Həyat</a>
                <div class="mobile-nav-sub">
                    <a href="#news" class="mobile-nav-sublink" data-i18n="nav_news">Son Xəbərlər</a>
                    <a href="#qarabag" class="mobile-nav-sublink" data-i18n="nav_qarabag">Qarabağ Zəfər Salnaməsi</a>
                    <a href="#gallery" class="mobile-nav-sublink" data-i18n="nav_gallery">Foto & Video Qalereya</a>
                    <a href="#certificates" class="mobile-nav-sublink" data-i18n="nav_certificates">Nailiyyətlər & Kuboklar</a>
                </div>
            </div>

            <a href="#contact" class="mobile-nav-link" data-i18n="nav_contact">Əlaqə</a>
        </nav>
    </div>"""

# Replace in index.html
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace desktop nav
html = re.sub(r'<nav class="header-nav" id="desktop-nav"[\s\S]*?</nav>', DESKTOP_NAV_HTML, html)

# Replace mobile nav drawer
html = re.sub(r'<div class="mobile-nav-drawer" id="mobile-nav"[\s\S]*?</div>\s*</div>', MOBILE_NAV_HTML, html)

# Bump cache version
html = re.sub(r'script\.js\?v=[^\"]+', 'script.js?v=20261106_38', html)
html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=20261106_38', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html with Variant 1 navigation.')
