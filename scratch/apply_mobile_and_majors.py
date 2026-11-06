#!/usr/bin/env python3
import re
import sys

def update_script_and_style():
    # 1. Update script.js
    with open("script.js", "r", encoding="utf-8") as f:
        js = f.read()

    # Add i18n keys for AZ
    az_marker = '    nav_certificates_sub: "Respublika spartakiadası və rəsmi diplomlar",\n  },'
    az_replacement = """    nav_certificates_sub: "Respublika spartakiadası və rəsmi diplomlar",
    nav_fbk: "Fənn Birləşmə Komissiyaları",
    nav_fbk_sub: "9 tədris-metodiki fənn komissiyası",
    majors_badge_count: "19 İxtisas",
  },"""
    if az_marker in js:
        js = js.replace(az_marker, az_replacement, 1)
        print("Added i18n keys to AZ")
    else:
        print("WARNING: az_marker not matched")

    # Add i18n keys for EN
    en_marker = '    nav_certificates_sub: "National spartakiad and official diplomas",\n  },'
    en_replacement = """    nav_certificates_sub: "National spartakiad and official diplomas",
    nav_fbk: "Subject Commissions",
    nav_fbk_sub: "9 specialized academic subject commissions",
    majors_badge_count: "19 Majors",
  },"""
    if en_marker in js:
        js = js.replace(en_marker, en_replacement, 1)
        print("Added i18n keys to EN")
    else:
        print("WARNING: en_marker not matched")

    # Add i18n keys for RU
    ru_marker = '    nav_certificates_sub: "Республиканская спартакиада и дипломы",\n  },'
    ru_replacement = """    nav_certificates_sub: "Республиканская спартакиада и дипломы",
    nav_fbk: "Предметные комиссии",
    nav_fbk_sub: "9 предметно-цикловых комиссий (ПЦК)",
    majors_badge_count: "19 Специальностей",
  },"""
    if ru_marker in js:
        js = js.replace(ru_marker, ru_replacement, 1)
        print("Added i18n keys to RU")
    else:
        print("WARNING: ru_marker not matched")

    # Update initScrollEngine to close on all mobile sublinks too
    old_links_close = """  links.forEach((link) => {
    link.addEventListener("click", () => {
      toggle.classList.remove("active");
      overlay.classList.remove("active");
      html.classList.remove("scroll-locked");
    });
  });"""
    new_links_close = """  const allMobileLinks = document.querySelectorAll(".mobile-nav-link, .mobile-nav-sublink");
  allMobileLinks.forEach((link) => {
    link.addEventListener("click", () => {
      toggle.classList.remove("active");
      overlay.classList.remove("active");
      html.classList.remove("scroll-locked");
    });
  });"""
    if old_links_close in js:
        js = js.replace(old_links_close, new_links_close, 1)
        print("Updated mobile nav link closing in initScrollEngine")
    else:
        print("WARNING: old_links_close not matched")

    # Update initStructureModule for toggleMajorsBtn
    old_init_struct_btns = """  const toggleTreeBtn = document.getElementById("toggle-tree-btn");
  const toggleCardsBtn = document.getElementById("toggle-cards-btn");"""
    new_init_struct_btns = """  const toggleTreeBtn = document.getElementById("toggle-tree-btn");
  const toggleCardsBtn = document.getElementById("toggle-cards-btn");
  const toggleMajorsBtn = document.getElementById("toggle-majors-btn");"""
    if old_init_struct_btns in js:
        js = js.replace(old_init_struct_btns, new_init_struct_btns, 1)
        print("Added toggleMajorsBtn in initStructureModule")
    else:
        print("WARNING: old_init_struct_btns not matched")

    # Update switchView and triggers in initStructureModule
    old_switch_view_block = """  // ─── 4. VIEW TOGGLE LOGIC ──────────────────────────────────────────
  function switchView(view) {
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
  toggleCardsBtn?.addEventListener("click", () => switchView("commissions"));"""

    new_switch_view_block = """  // ─── 4. VIEW TOGGLE LOGIC ──────────────────────────────────────────
  function switchView(view) {
    currentView = view;

    toggleTreeBtn?.classList.toggle("active", view === "tree");
    toggleTreeBtn?.setAttribute("aria-selected", view === "tree" ? "true" : "false");
    toggleCardsBtn?.classList.toggle("active", view === "commissions");
    toggleCardsBtn?.setAttribute("aria-selected", view === "commissions" ? "true" : "false");
    toggleMajorsBtn?.classList.toggle("active", view === "majors");
    toggleMajorsBtn?.setAttribute("aria-selected", view === "majors" ? "true" : "false");

    if (view === "tree") {
      treePane?.classList.add("active");
      commissionsPane?.classList.remove("active");
      renderTree();
    } else if (view === "commissions") {
      commissionsPane?.classList.add("active");
      treePane?.classList.remove("active");
      renderCommissionsGrid();
    } else if (view === "majors") {
      treePane?.classList.add("active");
      commissionsPane?.classList.remove("active");
      renderTree();
      setTimeout(() => {
        const majorsBlock = document.getElementById("tree-majors-block");
        if (majorsBlock) {
          const headerOffset = 90;
          const elementPosition = majorsBlock.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
          window.scrollTo({
            top: offsetPosition,
            behavior: "smooth"
          });
          majorsBlock.classList.remove("struct-highlight");
          void majorsBlock.offsetWidth;
          majorsBlock.classList.add("struct-highlight");
          setTimeout(() => majorsBlock.classList.remove("struct-highlight"), 3500);
        }
      }, 70);
    }
  }

  toggleTreeBtn?.addEventListener("click", () => switchView("tree"));
  toggleCardsBtn?.addEventListener("click", () => switchView("commissions"));
  toggleMajorsBtn?.addEventListener("click", () => switchView("majors"));"""

    if old_switch_view_block in js:
        js = js.replace(old_switch_view_block, new_switch_view_block, 1)
        print("Updated switchView logic in initStructureModule")
    else:
        print("WARNING: old_switch_view_block not matched")

    # Update navStructItems external triggers
    old_nav_triggers = """  // ─── 7. EXTERNAL TRIGGERS (Header Nav & About Jump Links) ──────────
  const navStructItems = document.querySelectorAll("[data-struct-cat], [data-struct-jump]");
  navStructItems.forEach((item) => {
    item.addEventListener("click", () => {
      const cat = item.getAttribute("data-struct-cat") || item.getAttribute("data-struct-jump");
      if (!cat) return;
      currentCategory = cat;

      // Activate Cards view and matching tab
      switchView("cards");
      subtabs.forEach((t) => {
        if (t.dataset.category === cat) t.classList.add("active");
        else t.classList.remove("active");
      });
      renderCards(cat);
    });
  });"""

    new_nav_triggers = """  // ─── 7. EXTERNAL TRIGGERS (Header Nav & Mobile Jump Links) ──────────
  const navStructItems = document.querySelectorAll("[data-struct-cat], [data-struct-jump]");
  navStructItems.forEach((item) => {
    item.addEventListener("click", () => {
      const cat = item.getAttribute("data-struct-cat") || item.getAttribute("data-struct-jump");
      if (!cat) return;
      currentCategory = cat;

      // Close mobile drawer if open
      const mobileNav = document.getElementById("mobile-nav");
      const mobileToggle = document.getElementById("mobile-toggle");
      if (mobileNav && mobileNav.classList.contains("active")) {
        mobileNav.classList.remove("active");
        if (mobileToggle) mobileToggle.classList.remove("active");
        document.documentElement.classList.remove("scroll-locked");
      }

      if (cat === "majors") {
        // Go directly to MAJORS (19 İxtisas), NOT commissions!
        switchView("majors");
      } else if (cat === "commissions" || cat === "fbk") {
        // Go directly to FƏNN BİRLƏŞMƏLƏRİ (FBK)!
        switchView("commissions");
        setTimeout(() => {
          const commEl = document.getElementById("struct-commissions-view");
          if (commEl) {
            const headerOffset = 90;
            const elementPosition = commEl.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
            window.scrollTo({
              top: offsetPosition,
              behavior: "smooth"
            });
          }
        }, 70);
      } else if (cat === "departments") {
        switchView("tree");
        setTimeout(() => {
          const deptEl = document.querySelector(".tree-wings-container");
          if (deptEl) {
            const headerOffset = 90;
            const elementPosition = deptEl.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
            window.scrollTo({
              top: offsetPosition,
              behavior: "smooth"
            });
          }
        }, 70);
      } else {
        // leadership / default
        switchView("tree");
        setTimeout(() => {
          const sec = document.getElementById("structure");
          if (sec) {
            const headerOffset = 80;
            const elementPosition = sec.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
            window.scrollTo({
              top: offsetPosition,
              behavior: "smooth"
            });
          }
        }, 70);
      }
    });
  });"""

    if old_nav_triggers in js:
        js = js.replace(old_nav_triggers, new_nav_triggers, 1)
        print("Updated navStructItems external triggers in script.js")
    else:
        print("WARNING: old_nav_triggers not matched")

    # Update languageChanged in initStructureModule
    old_lang_re = """  document.addEventListener("languageChanged", () => {
    renderCategoriesCount();
    if (currentView === "tree") {
      renderTree();
    } else {
      renderCards(currentCategory);
    }
  });"""

    new_lang_re = """  document.addEventListener("languageChanged", () => {
    renderCategoriesCount();
    if (currentView === "tree" || currentView === "majors") {
      renderTree();
    } else {
      renderCommissionsGrid();
    }
  });"""

    if old_lang_re in js:
        js = js.replace(old_lang_re, new_lang_re, 1)
        print("Updated languageChanged in initStructureModule")
    else:
        print("WARNING: old_lang_re not matched")

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js)
    with open("scratch/script_working_backup.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("script.js and scratch/script_working_backup.js updated successfully")

    # 2. Update style.css
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Mobile nav header & icon styles
    old_mobile_sublink = """.mobile-nav-sublink {
  padding: 9px 14px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text-secondary);
  border-radius: var(--radius-xs);
  transition: all var(--transition);
}

.mobile-nav-sublink:hover {
  background: var(--bg-alt);
  color: var(--accent);
}"""

    new_mobile_sublink = """.mobile-nav-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 16px;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--accent);
  background: rgba(184, 147, 74, 0.08);
  border-radius: var(--radius-sm);
  border-left: 3px solid var(--gold);
  margin-top: 6px;
  letter-spacing: 0.02em;
}

.mobile-nav-icon {
  font-size: 1.15rem;
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.mobile-sub-bullet {
  font-size: 0.85rem;
  opacity: 0.85;
}

.mobile-nav-sublink {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-secondary);
  border-radius: var(--radius-xs);
  transition: all var(--transition);
}

.mobile-nav-sublink:hover,
.mobile-nav-sublink:active {
  background: var(--bg-alt);
  color: var(--gold);
}

.tree-majors-section.struct-highlight {
  box-shadow: 0 0 0 3px var(--gold), 0 16px 40px rgba(184, 147, 74, 0.35) !important;
  animation: majorsPulse 1.8s ease-in-out infinite;
}

@keyframes majorsPulse {
  0%, 100% {
    box-shadow: 0 0 0 3px var(--gold), 0 16px 40px rgba(184, 147, 74, 0.35);
  }
  50% {
    box-shadow: 0 0 0 6px var(--gold), 0 22px 55px rgba(184, 147, 74, 0.6);
  }
}"""

    if old_mobile_sublink in css:
        css = css.replace(old_mobile_sublink, new_mobile_sublink, 1)
        print("Updated style.css mobile nav and majors pulse styles")
    else:
        print("WARNING: old_mobile_sublink not matched in style.css")

    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("style.css updated successfully")

update_script_and_style()
