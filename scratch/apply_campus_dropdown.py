import os, sys, re

base_dir = "/Users/konul/Documents/esas2 copy 2"

# 1. READ FILES
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html_src = f.read()

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

# 2. UPDATE DESKTOP NAV IN INDEX.HTML
# 2.1 Remove the redundant campus item from inside the Struktur dropdown
struct_campus_item = '''                        <a href="#campus-navigator" class="nav-dropdown-item" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><line x1="9" y1="6" x2="9" y2="6.01"></line><line x1="15" y1="6" x2="15" y2="6.01"></line><line x1="9" y1="10" x2="9" y2="10.01"></line><line x1="15" y1="10" x2="15" y2="10.01"></line><line x1="9" y1="14" x2="9" y2="14.01"></line><line x1="15" y1="14" x2="15" y2="14.01"></line><line x1="9" y1="18" x2="15" y2="18"></line></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title" data-i18n="nav_campus">Kampus & Otaqlar</span>
                                <span class="nav-dd-sub" data-i18n="nav_campus_sub">5 mərtəbəli bina naviqasiyası</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>\n'''

if struct_campus_item in html_src:
    html_src = html_src.replace(struct_campus_item, "")
    print("Removed campus item from inside Struktur dropdown.")

# 2.2 Replace desktop `<a href="#campus-navigator" class="nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>` with nav-dropdown
desktop_campus_trigger = '<a href="#campus-navigator" class="nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>'

desktop_campus_dropdown = '''<div class="nav-dropdown">
                    <a href="#campus-navigator" class="nav-link nav-dropdown-trigger" aria-haspopup="true">
                        <span data-i18n="nav_campus">Kampus & Otaqlar</span>
                        <svg class="nav-chevron" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </a>
                    <div class="nav-dropdown-menu" role="menu" aria-label="Kampus mərtəbələri">
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="1" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title">1-ci Mərtəbə</span>
                                <span class="nav-dd-sub">İdman kompleksi, Kimya & Rabitə lab</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="2" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><line x1="9" y1="6" x2="9" y2="6.01"></line><line x1="15" y1="6" x2="15" y2="6.01"></line><line x1="9" y1="10" x2="9" y2="10.01"></line><line x1="15" y1="10" x2="15" y2="10.01"></line></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title">2-ci Mərtəbə</span>
                                <span class="nav-dd-sub">Rəhbərlik, Kitabxana 206 & İKT otaqları</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="3" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title">3-cü Mərtəbə</span>
                                <span class="nav-dd-sub">Fizika laboratoriyası & 16 Auditoriya</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="4" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title">4-cü Mərtəbə</span>
                                <span class="nav-dd-sub">Poçt laboratoriyası, İKT & 17 Auditoriya</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="5" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title">5-ci Mərtəbə</span>
                                <span class="nav-dd-sub">Kompüter texnologiyası & 18 Auditoriya</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                        <a href="#campus-navigator" class="nav-dropdown-item" data-campus-floor="all" role="menuitem">
                            <span class="nav-dd-icon">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                            </span>
                            <span class="nav-dd-text">
                                <span class="nav-dd-title">Bütün Mərtəbələr</span>
                                <span class="nav-dd-sub">5 mərtəbə üzrə bütün 80+ otaq</span>
                            </span>
                            <svg class="nav-dd-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                    </div>
                </div>'''

if desktop_campus_trigger in html_src:
    html_src = html_src.replace(desktop_campus_trigger, desktop_campus_dropdown, 1)
    print("Replaced desktop Kampus & Otaqlar link with full dropdown!")

# 2.3 Update MOBILE NAV
# Remove redundant sublink from inside Struktur group in mobile
mob_struct_campus = '                    <a href="#campus-navigator" class="mobile-nav-sublink" data-i18n="nav_campus">Kampus & Otaqlar</a>\n'
if mob_struct_campus in html_src:
    html_src = html_src.replace(mob_struct_campus, "")
    print("Removed mobile campus sublink from Struktur group.")

# Replace `<a href="#campus-navigator" class="mobile-nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>` with mobile-nav-group
mob_campus_old = '<a href="#campus-navigator" class="mobile-nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>'
mob_campus_group = '''<div class="mobile-nav-group">
                <a href="#campus-navigator" class="mobile-nav-link" data-i18n="nav_campus">Kampus & Otaqlar</a>
                <div class="mobile-nav-sub">
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="1">1-ci Mərtəbə (İdman & Lab)</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="2">2-ci Mərtəbə (Rəhbərlik & Kitabxana)</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="3">3-cü Mərtəbə (Fizika & 16 Otaq)</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="4">4-cü Mərtəbə (Poçt & 17 Otaq)</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="5">5-ci Mərtəbə (Kompüter & 18 Otaq)</a>
                    <a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="all">Bütün Mərtəbələr (80+ Otaq)</a>
                </div>
            </div>'''

if mob_campus_old in html_src:
    html_src = html_src.replace(mob_campus_old, mob_campus_group, 1)
    print("Replaced mobile Kampus & Otaqlar link with collapsible floor group!")

# Bump cache version to v=20261106_33
html_src = re.sub(r'style\.css\?v=[a-zA-Z0-9_]+', 'style.css?v=20261106_33', html_src)
html_src = re.sub(r'script\.js\?v=[a-zA-Z0-9_]+', 'script.js?v=20261106_33', html_src)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_src)
print("index.html updated successfully.")

# 3. UPDATE SCRIPT.JS TO HANDLE [data-campus-floor]
# Check if switchCampusFloor is in script.js
if 'data-campus-floor' not in js_src:
    # Inside initCampusNavigatorModule, add switchCampusFloor and event listeners
    target_bind = '  // Bind Floor Buttons'
    replacement_bind = '''  function switchFloor(floor) {
    if (!floor) return;
    activeFloor = String(floor);
    floorBtns.forEach(b => {
      const isCurrent = b.getAttribute("data-floor") === activeFloor;
      b.classList.toggle("active", isCurrent);
      b.setAttribute("aria-selected", isCurrent ? "true" : "false");
    });
    updateFloorBanner();
    renderRooms();
  }
  window.switchCampusFloor = switchFloor;

  // Bind Header Dropdown & Mobile Nav Floor links
  document.querySelectorAll("[data-campus-floor]").forEach(item => {
    item.addEventListener("click", () => {
      const fl = item.getAttribute("data-campus-floor");
      switchFloor(fl);

      // Close mobile drawer if open
      const mobileNav = document.getElementById("mobile-nav");
      if (mobileNav && mobileNav.classList.contains("active")) {
        mobileNav.classList.remove("active");
        document.body.classList.remove("nav-open");
      }

      // Smooth scroll to campus section
      const sec = document.getElementById("campus-navigator");
      if (sec) {
        sec.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  // Bind Floor Buttons'''
    js_src = js_src.replace(target_bind, replacement_bind, 1)
    print("Added data-campus-floor listeners and window.switchCampusFloor to script.js")

with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(js_src)

with open(os.path.join(base_dir, "scratch/script_working_backup.js"), "w", encoding="utf-8") as f:
    f.write(js_src)

print("script.js and backup updated successfully.")
