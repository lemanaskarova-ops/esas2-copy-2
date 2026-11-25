/* ==========================================================================
   BDRNK UI Workspace Router & Tailwind Theme Bridge (ui-tabs.js)
   Additive layer compatible 100% with script.js & Global Search.
   ========================================================================== */

(function initBdrnkWorkspaceUI() {
  "use strict";

  const VALID_TABS = [
    "about",
    "admission",
    "structure",
    "majors",
    "science",
    "library",
    "lectures",
    "international",
    "students",
    "certificates",
    "news",
    "contact",
    "all",
  ];

  // Backward-compatible aliases so legacy ?tab=... links & search entries resolve cleanly
  const TAB_ALIASES = {
    home: { tab: "about" },
    qebul: { tab: "admission" },
    "telebe-qebulu": { tab: "admission" },
    abituriyent: { tab: "admission" },
    "library-lectures": { tab: "library", libView: "lectures", anchor: "library-lectures-section" },
    "honor-students": { tab: "students", anchor: "honor-students" },
    "teacher-certificates": { tab: "certificates", anchor: "teacher-certificates" },
    campus: { tab: "about", anchor: "campus-navigator", floor: "all" },
    qarabag: { tab: "about", anchor: "qarabag" },
    gallery: { tab: "news", anchor: "gallery" },
    academics: { tab: "science" },
    achievements: { tab: "students" },
    media: { tab: "news" },
  };

  // Map every section ID or sub-anchor in index.html to its exact canonical tab
  const TARGET_TO_TAB = {
    hero: "about",
    "portal-directory": "about",
    "executive-hub": "about",
    about: "about",
    "about-mvv-anchor": "about",
    "labor-market-conference": "about",
    "campus-navigator": "about",
    "campus-all-floors": "about",
    campus: "about",
    "campus-floor-1": "about",
    "campus-floor-2": "about",
    "campus-floor-3": "about",
    "campus-floor-4": "about",
    "campus-floor-5": "about",
    qarabag: "about",
    memorial: "about",
    graduates: "about",

    admission: "admission",
    "admission-overview": "admission",
    "admission-roadmap": "admission",
    "admission-docs": "admission",
    "admission-majors": "admission",
    "admission-faq": "admission",

    structure: "structure",
    "struct-tree-view": "structure",
    "struct-cards-view": "structure",
    "honored-staff-highlight": "structure",

    majors: "majors",
    "majors-section": "majors",
    "tree-majors-block": "majors",
    "education-process-section": "majors",
    roadmap: "majors",

    science: "science",
    "science-portal": "science",
    "science-textbooks-section": "science",
    "science-articles-anchor": "science",
    "science-methodical-hub": "science",
    "science-conferences-section": "science",
    "science-seminars-section": "science",
    "science-open-lessons-section": "science",

    library: "library",
    "library-books-pane": "library",
    "lib-master-switcher": "library",
    "library-lectures": "library",
    "library-lectures-section": "library",

    lectures: "lectures",
    "lecture-studio": "lectures",
    "lectures-grid": "lectures",

    international: "international",
    "intl-cooperation": "international",
    "intl-memorandums": "international",
    "intl-conferences": "international",
    "intl-certificates": "international",

    "honor-students": "students",
    "student-projects-section": "students",
    "sports-trophies": "students",
    "trophy-stage": "students",
    "student-competitions-section": "students",

    "teacher-certificates": "certificates",
    certificates: "certificates",
    "cert-grid": "certificates",

    news: "news",
    gallery: "news",

    contact: "contact",
    "contact-form": "contact",
    faq: "contact",
    "faq-accordion": "contact",
  };

  let activeTab = "about";

  // ── 1. Tailwind `.dark` <-> `script.js` `.dark-mode` Sync ─────────────────
  function syncTailwindDarkClass() {
    const html = document.documentElement;
    const isDark =
      html.classList.contains("dark-mode") ||
      html.getAttribute("data-theme") === "dark";
    html.classList.toggle("dark", isDark);
  }

  syncTailwindDarkClass();
  const themeObserver = new MutationObserver(syncTailwindDarkClass);
  themeObserver.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["class", "data-theme"],
  });

  // ── 2. Tab State Management ──────────────────────────────────────────────
  function findTabForElement(el) {
    if (!el || typeof el.closest !== "function") return null;
    const panel = el.closest("[data-tab-panel]");
    return panel ? panel.getAttribute("data-tab-panel") : null;
  }

  function animateStuckStatCounters() {
    document
      .querySelectorAll(".tab-workspace-panel.is-active .stat-number[data-target]")
      .forEach((el) => {
        const target = parseInt(el.getAttribute("data-target"), 10);
        if (Number.isNaN(target)) return;
        const raw = (el.textContent || "").replace(/[^\d]/g, "");
        const currentNum = parseInt(raw, 10);
        if (el.dataset.tabAnimated === "true" || currentNum === target) return;
        el.dataset.tabAnimated = "true";
        const startVal = Number.isNaN(currentNum) ? 0 : currentNum;
        const duration = 900;
        const startTime = performance.now();
        function step(now) {
          const t = Math.min(1, (now - startTime) / duration);
          const eased = 1 - Math.pow(1 - t, 3);
          const val = Math.round(startVal + (target - startVal) * eased);
          el.textContent = String(val);
          if (t < 1) {
            requestAnimationFrame(step);
          } else {
            el.textContent = String(target);
          }
        }
        requestAnimationFrame(step);
      });
  }

  function revealActiveElements() {
    if (typeof window.syncSafeReveals === "function") {
      try {
        window.syncSafeReveals();
      } catch (e) { }
    }
    document
      .querySelectorAll(".tab-workspace-panel.is-active .reveal, .tab-workspace-panel.is-active .roadmap-item")
      .forEach((node) => {
        node.classList.add("visible");
      });
    animateStuckStatCounters();
    try {
      window.dispatchEvent(new Event("scroll"));
    } catch (e) { }
  }

  const originalScrollIntoView = Element.prototype.scrollIntoView;

  function resolveAliasConfig(rawTabId) {
    if (!rawTabId) return { tab: "about" };
    if (rawTabId.startsWith("campus-floor-")) {
      return { tab: "about", anchor: "campus-navigator", floor: rawTabId.replace("campus-floor-", "") };
    }
    if (TAB_ALIASES[rawTabId]) {
      return TAB_ALIASES[rawTabId];
    }
    if (TARGET_TO_TAB[rawTabId]) {
      return { tab: TARGET_TO_TAB[rawTabId], anchor: rawTabId };
    }
    return { tab: rawTabId };
  }

  function setActiveTab(tabId, options = {}) {
    const aliasCfg = resolveAliasConfig(tabId);
    const resolvedTab = aliasCfg.tab;
    const autoFloor = options.floor || aliasCfg.floor || null;
    const autoLibView = options.libView || aliasCfg.libView || null;

    const nextTab = VALID_TABS.includes(resolvedTab) ? resolvedTab : "about";
    const {
      scrollToTop = false,
      updateUrl = true,
      pushHistory = false,
      focusAnchor = aliasCfg.anchor || null,
    } = options;
    const prevTab = activeTab;
    activeTab = nextTab;

    if (autoFloor && typeof window.switchCampusFloor === "function") {
      try {
        window.switchCampusFloor(autoFloor);
      } catch (e) { }
    }

    // Toggle category panels & pause playing videos inside hidden panels
    document.querySelectorAll("[data-tab-panel]").forEach((panel) => {
      const panelName = panel.getAttribute("data-tab-panel");
      const shouldShow = nextTab === "all" || panelName === nextTab;
      panel.classList.toggle("is-active", shouldShow);
      panel.setAttribute("aria-hidden", shouldShow ? "false" : "true");
      if (!shouldShow) {
        panel.querySelectorAll("video").forEach((video) => {
          if (!video.paused && typeof video.pause === "function") {
            try {
              video.pause();
            } catch (e) { }
          }
        });
      }
    });

    // If opening library vs library-lectures, toggle inner switcher accurately
    if (autoLibView === "lectures") {
      const lecBtn = document.querySelector('#lib-master-switcher [data-view="lectures"]');
      if (lecBtn && typeof lecBtn.click === "function") lecBtn.click();
    } else if (autoLibView === "books" || (nextTab === "library" && prevTab !== "library" && !autoLibView)) {
      const booksBtn = document.querySelector('#lib-master-switcher [data-view="books"]');
      if (booksBtn && typeof booksBtn.click === "function") booksBtn.click();
    }

    // Update Workspace Tab Pills (roving tabindex for WAI-ARIA tablist)
    document.querySelectorAll("[data-workspace-tab]").forEach((btn) => {
      const btnTab = btn.getAttribute("data-workspace-tab");
      const isMatch = btnTab === nextTab || (nextTab === "structure" && btnTab === "about" && btn.classList.contains("workspace-tab-btn"));
      btn.classList.toggle("is-active", isMatch);
      btn.setAttribute("aria-selected", isMatch ? "true" : "false");
      if (btn.classList.contains("workspace-tab-btn")) {
        btn.setAttribute("tabindex", isMatch ? "0" : "-1");
      }
    });

    // Active-tab indicator in URL (?tab=...) without forcing page reload
    if (updateUrl && window.history && typeof window.history.replaceState === "function") {
      try {
        const url = new URL(window.location.href);
        if (nextTab === "about" && !focusAnchor) {
          url.searchParams.delete("tab");
        } else {
          url.searchParams.set("tab", nextTab);
        }
        const nextUrl = url.pathname + url.search + (focusAnchor ? "#" + focusAnchor : "");
        const currentRel = window.location.pathname + window.location.search + window.location.hash;
        if (pushHistory && typeof window.history.pushState === "function" && (prevTab !== nextTab || nextUrl !== currentRel)) {
          window.history.pushState({ tab: nextTab, anchor: focusAnchor }, "", nextUrl);
        } else {
          window.history.replaceState({ tab: nextTab, anchor: focusAnchor }, "", nextUrl);
        }
      } catch (e) { }
    }

    // Center active tab pill horizontally on mobile scroll bar
    const activeBtn = document.querySelector(`[data-workspace-tab="${nextTab}"].workspace-tab-btn`);
    if (activeBtn && typeof originalScrollIntoView === "function") {
      try {
        originalScrollIntoView.call(activeBtn, { behavior: "smooth", block: "nearest", inline: "center" });
      } catch (e) { }
    }

    // Mount #tree-majors-block inside dedicated #majors-tab-mount with full interactivity
    function syncMajorsMount() {
      const mount = document.getElementById("majors-tab-mount");
      if (!mount) return;
      if (typeof window.renderMajorsCatalog === "function") {
        window.renderMajorsCatalog(mount);
        return;
      }
      let block = document.getElementById("tree-majors-block");
      if (!block && typeof window.switchStructureView === "function") {
        try {
          window.switchStructureView("tree");
        } catch (e) { }
        block = document.getElementById("tree-majors-block");
      }
      if (block) {
        if (!mount.querySelector(".majors-catalog-table") || mount.children.length === 0) {
          const clone = block.cloneNode(true);
          clone.id = "tree-majors-block-mount";
          mount.replaceChildren(clone);
          clone.querySelectorAll(".majors-tab-btn").forEach((btn) => {
            btn.addEventListener("click", () => {
              const view = btn.dataset.majorView;
              clone.querySelectorAll(".majors-tab-btn").forEach((b) => b.classList.remove("active"));
              btn.classList.add("active");
              clone.querySelectorAll(".majors-pane").forEach((p) => p.classList.remove("active"));
              const target = clone.querySelector(`#majors-pane-${view}`);
              if (target) target.classList.add("active");
            });
          });
        }
      }
    }
    window.syncMajorsMount = syncMajorsMount;
    syncMajorsMount();

    requestAnimationFrame(() => {
      revealActiveElements();
      setTimeout(revealActiveElements, 120);

      const topLevelTargets = [
        nextTab,
        "hero",
        "about",
        "structure",
        "admission",
        "majors",
        "majors-section",
        "science",
        "library",
        "lectures",
        "international",
        "students",
        "certificates",
        "news",
        "contact",
        "panel-" + nextTab,
        "about-overview"
      ];

      const isTopLevel = !focusAnchor || topLevelTargets.includes(focusAnchor);

      if (isTopLevel || scrollToTop || prevTab !== nextTab) {
        window.scrollTo({ top: 0, behavior: "smooth" });
        return;
      }

      const target = document.getElementById(focusAnchor);
      if (target) {
        setTimeout(() => {
          const headerH = (document.getElementById("site-header")?.offsetHeight || 72) + 24;
          const y = target.getBoundingClientRect().top + window.scrollY - headerH;
          window.scrollTo({ top: Math.max(0, y), behavior: "smooth" });
        }, 80);
      } else {
        window.scrollTo({ top: 0, behavior: "smooth" });
      }
    });
  }

  window.switchWorkspaceTab = setActiveTab;

  // ── 3. Seamless Compatibility with script.js scrollIntoView & Helpers ────
  Element.prototype.scrollIntoView = function patchedScrollIntoView(arg) {
    const ownerTab = findTabForElement(this);
    if (ownerTab && activeTab !== "all" && activeTab !== ownerTab) {
      setActiveTab(ownerTab, { scrollToTop: false, updateUrl: true });
      requestAnimationFrame(() => {
        originalScrollIntoView.call(this, arg);
      });
      return;
    }
    return originalScrollIntoView.call(this, arg);
  };

  function closeMobileDrawerIfOpen() {
    const mobileNav = document.getElementById("mobile-nav");
    const mobileToggle = document.getElementById("mobile-toggle");
    if (mobileNav && mobileNav.classList.contains("active")) {
      mobileNav.classList.remove("active");
      mobileToggle?.classList.remove("active");
      mobileToggle?.setAttribute("aria-expanded", "false");
      document.documentElement.classList.remove("scroll-locked");
    }
  }

  function resolveTabForTarget(rawId) {
    if (!rawId) return null;
    const clean = rawId.replace(/^#/, "");
    if (TARGET_TO_TAB[clean]) return TARGET_TO_TAB[clean];
    const el = document.getElementById(clean);
    return el ? findTabForElement(el) : null;
  }

  // Intercept clicks on workspace tabs, library subview buttons, and in-page anchors
  document.addEventListener("click", (e) => {
    const libSubTrigger = e.target.closest("[data-lib-subview]");
    if (libSubTrigger) {
      e.preventDefault();
      const viewMode = libSubTrigger.getAttribute("data-lib-subview") || "books";
      setActiveTab("library", {
        scrollToTop: false,
        updateUrl: true,
        pushHistory: true,
        libView: viewMode,
        focusAnchor: "lib-master-switcher",
      });
      return;
    }

    const tabTrigger = e.target.closest("[data-workspace-tab]");
    if (tabTrigger) {
      // Allow Ctrl/Cmd/Shift/Middle-click to open as a new browser tab natively
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button === 1) return;
      e.preventDefault();
      e.stopPropagation();
      const targetTab = tabTrigger.getAttribute("data-workspace-tab");
      const focusAnchor = tabTrigger.getAttribute("data-focus-anchor") || null;
      closeMobileDrawerIfOpen();
      setActiveTab(targetTab, { scrollToTop: true, updateUrl: true, pushHistory: true, focusAnchor });
      return;
    }

    const anchor = e.target.closest('a[href^="#"]');
    if (!anchor) return;
    const href = anchor.getAttribute("href");
    if (!href || href === "#") return;
    const targetId = href.slice(1);
    const ownerTab = resolveTabForTarget(targetId);

    // Special campus floor shortcut anchors (#campus-floor-1 .. #campus-floor-5, #campus-all-floors)
    if (targetId.startsWith("campus-floor-") && typeof window.switchCampusFloor === "function") {
      e.preventDefault();
      closeMobileDrawerIfOpen();
      setActiveTab("about", { scrollToTop: false, updateUrl: true, focusAnchor: "campus-navigator", floor: targetId.replace("campus-floor-", "") });
      window.switchCampusFloor(targetId.replace("campus-floor-", ""));
      return;
    }
    if (targetId === "campus-all-floors" && typeof window.switchCampusFloor === "function") {
      e.preventDefault();
      closeMobileDrawerIfOpen();
      setActiveTab("about", { scrollToTop: false, updateUrl: true, focusAnchor: "campus-navigator", floor: "all" });
      window.switchCampusFloor("all");
      return;
    }

    // Intercept library vs library-lectures to toggle books / lectures pane
    if (targetId === "library") {
      const booksBtn = document.querySelector('#lib-master-switcher [data-view="books"]');
      if (booksBtn && typeof booksBtn.click === "function") booksBtn.click();
    } else if (targetId === "library-lectures" || targetId === "library-lectures-section") {
      const lecBtn = document.querySelector('#lib-master-switcher [data-view="lectures"]');
      if (lecBtn && typeof lecBtn.click === "function") lecBtn.click();
    }

    if (ownerTab && activeTab !== "all" && activeTab !== ownerTab) {
      e.preventDefault();
      e.stopPropagation();
      closeMobileDrawerIfOpen();
      const isSectionLevel = targetId === ownerTab || targetId === "structure" || targetId === "admission" || targetId === "about" || targetId === "majors-section";
      setActiveTab(ownerTab, { scrollToTop: isSectionLevel, updateUrl: true, pushHistory: true, focusAnchor: isSectionLevel ? null : targetId });
      return;
    } else if (ownerTab && (activeTab === ownerTab || activeTab === "all")) {
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        e.preventDefault();
        closeMobileDrawerIfOpen();
        const headerH = (document.getElementById("site-header")?.offsetHeight || 72) + 24;
        const y = targetEl.getBoundingClientRect().top + window.scrollY - headerH;
        window.scrollTo({ top: Math.max(0, y), behavior: "smooth" });
      }
    }
  }, true);

  // WAI-ARIA keyboard navigation on #workspace-tabs-bar [role="tablist"]
  document.addEventListener("keydown", (e) => {
    const tabBtn = e.target.closest("#workspace-tabs-bar .workspace-tab-btn[data-workspace-tab]");
    if (!tabBtn) return;
    const tabList = tabBtn.closest('[role="tablist"]');
    if (!tabList) return;
    const tabs = Array.from(tabList.querySelectorAll('.workspace-tab-btn[data-workspace-tab]'));
    const idx = tabs.indexOf(tabBtn);
    if (idx === -1 || !tabs.length) return;

    let nextIdx = -1;
    if (e.key === "ArrowRight") {
      nextIdx = (idx + 1) % tabs.length;
    } else if (e.key === "ArrowLeft") {
      nextIdx = (idx - 1 + tabs.length) % tabs.length;
    } else if (e.key === "Home") {
      nextIdx = 0;
    } else if (e.key === "End") {
      nextIdx = tabs.length - 1;
    }

    if (nextIdx >= 0) {
      e.preventDefault();
      const targetBtn = tabs[nextIdx];
      targetBtn.focus();
      const targetTab = targetBtn.getAttribute("data-workspace-tab");
      setActiveTab(targetTab, { scrollToTop: false, updateUrl: true, pushHistory: true });
    }
  });

  document.addEventListener("DOMContentLoaded", () => {
    // Trigger tab activation on initial URL query (?tab=...) or #hash (supporting aliases)
    let initialTab = "about";
    let initialAnchor = null;
    try {
      const params = new URLSearchParams(window.location.search);
      const qTab = params.get("tab");
      if (qTab && (VALID_TABS.includes(qTab) || TAB_ALIASES[qTab] || qTab.startsWith("campus-floor-"))) {
        initialTab = qTab;
      }
      if (window.location.hash && window.location.hash.length > 1) {
        const hashId = window.location.hash.slice(1);
        const mapped = resolveTabForTarget(hashId);
        if (mapped) {
          initialTab = mapped;
          initialAnchor = hashId;
        }
      }
    } catch (e) { }

    setActiveTab(initialTab, {
      scrollToTop: false,
      updateUrl: false,
      focusAnchor: initialAnchor,
    });
  });

  window.addEventListener("hashchange", () => {
    const hashId = (window.location.hash || "").replace(/^#/, "");
    if (!hashId) return;
    const mapped = resolveTabForTarget(hashId);
    if (mapped && activeTab !== "all" && activeTab !== mapped) {
      setActiveTab(mapped, { scrollToTop: false, updateUrl: false, pushHistory: false, focusAnchor: hashId });
    }
  });

  window.addEventListener("popstate", (e) => {
    let popTab = "about";
    let popAnchor = null;
    try {
      if (e.state && e.state.tab && (VALID_TABS.includes(e.state.tab) || TAB_ALIASES[e.state.tab])) {
        popTab = e.state.tab;
        popAnchor = e.state.anchor || null;
      } else {
        const params = new URLSearchParams(window.location.search);
        const qTab = params.get("tab");
        if (qTab && (VALID_TABS.includes(qTab) || TAB_ALIASES[qTab] || qTab.startsWith("campus-floor-"))) {
          popTab = qTab;
        } else if (window.location.hash && window.location.hash.length > 1) {
          const hashId = window.location.hash.slice(1);
          const mapped = resolveTabForTarget(hashId);
          if (mapped) {
            popTab = mapped;
            popAnchor = hashId;
          }
        }
      }
    } catch (err) { }
    setActiveTab(popTab, { scrollToTop: false, updateUrl: false, pushHistory: false, focusAnchor: popAnchor });
  });

  // Horizontal wheel glide for scrollable #desktop-nav
  document.addEventListener("DOMContentLoaded", () => {
    const navStrip = document.getElementById("desktop-nav");
    if (navStrip) {
      navStrip.addEventListener(
        "wheel",
        (e) => {
          if (navStrip.scrollWidth <= navStrip.clientWidth) return;
          if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
            navStrip.scrollLeft += e.deltaY;
            e.preventDefault();
          }
        },
        { passive: false }
      );

      let isDown = false;
      let startX = 0;
      let scrollLeft = 0;
      let moved = false;

      navStrip.addEventListener("mousedown", (e) => {
        if (e.button !== 0) return;
        isDown = true;
        moved = false;
        startX = e.pageX - navStrip.offsetLeft;
        scrollLeft = navStrip.scrollLeft;
      });
      window.addEventListener("mouseup", () => {
        isDown = false;
      });
      navStrip.addEventListener("mousemove", (e) => {
        if (!isDown) return;
        const x = e.pageX - navStrip.offsetLeft;
        const walk = x - startX;
        if (Math.abs(walk) > 4) moved = true;
        navStrip.scrollLeft = scrollLeft - walk;
      });
      navStrip.addEventListener(
        "click",
        (e) => {
          if (moved) {
            e.preventDefault();
            e.stopPropagation();
            moved = false;
          }
        },
        true
      );
    }
  });
})();
