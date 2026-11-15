/* ==========================================================================
   BDRNK UI Workspace Router & Tailwind Theme Bridge (ui-tabs.js)
   Additive layer compatible 100% with script.js & Global Search.
   ========================================================================== */

(function initBdrnkWorkspaceUI() {
  "use strict";

  const VALID_TABS = [
    "about",
    "structure",
    "majors",
    "lectures",
    "library",
    "library-lectures",
    "science",
    "honor-students",
    "teacher-certificates",
    "campus",
    "news",
    "qarabag",
    "gallery",
    "contact",
    "all",
  ];

  // Map every section ID or sub-anchor in index.html to its exact category tab
  const TARGET_TO_TAB = {
    hero: "about",
    "executive-hub": "about",
    about: "about",
    graduates: "about",

    structure: "structure",
    "struct-tree-view": "structure",
    "struct-cards-view": "structure",

    majors: "majors",
    "majors-section": "majors",
    "tree-majors-block": "majors",

    lectures: "lectures",
    "lecture-studio": "lectures",

    library: "library",
    "library-books-pane": "library",
    "lib-master-switcher": "library",

    "library-lectures": "library-lectures",
    "library-lectures-section": "library-lectures",

    science: "science",
    roadmap: "science",

    "honor-students": "honor-students",
    "teacher-certificates": "teacher-certificates",

    certificates: "honor-students",
    "sports-trophies": "honor-students",
    "trophy-stage": "honor-students",

    "campus-navigator": "campus",
    "campus-all-floors": "campus",
    campus: "campus",

    "campus-floor-1": "campus",
    "campus-floor-2": "campus",
    "campus-floor-3": "campus",
    "campus-floor-4": "campus",
    "campus-floor-5": "campus",

    news: "news",
    qarabag: "qarabag",
    memorial: "qarabag",
    gallery: "gallery",

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
      .querySelectorAll(".tab-workspace-panel.is-active .reveal")
      .forEach((node) => {
        node.classList.add("visible");
      });
    animateStuckStatCounters();
    try {
      window.dispatchEvent(new Event("scroll"));
    } catch (e) { }
  }

  const originalScrollIntoView = Element.prototype.scrollIntoView;

  function setActiveTab(tabId, options = {}) {
    let resolvedTab = tabId;
    let autoFloor = null;
    if (tabId && tabId.startsWith("campus-floor-")) {
      autoFloor = tabId.replace("campus-floor-", "");
      resolvedTab = "campus";
    }

    const nextTab = VALID_TABS.includes(resolvedTab) ? resolvedTab : "about";
    const {
      scrollToTop = false,
      updateUrl = true,
      pushHistory = false,
      focusAnchor = null,
    } = options;
    const prevTab = activeTab;
    activeTab = nextTab;

    if (autoFloor && typeof window.switchCampusFloor === "function") {
      try {
        window.switchCampusFloor(autoFloor);
      } catch (e) { }
    } else if (nextTab === "campus" && !autoFloor && typeof window.switchCampusFloor === "function") {
      try {
        window.switchCampusFloor("all");
      } catch (e) { }
    }

    // Toggle category panels & pause playing videos inside hidden panels
    const actualPanelName = nextTab === "library-lectures" ? "library" : nextTab;
    document.querySelectorAll("[data-tab-panel]").forEach((panel) => {
      const panelName = panel.getAttribute("data-tab-panel");
      const shouldShow = nextTab === "all" || panelName === actualPanelName;
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

    // If opening library vs library-lectures, automatically toggle inner switcher
    if (nextTab === "library") {
      const booksBtn = document.querySelector('#lib-master-switcher [data-view="books"]');
      if (booksBtn && typeof booksBtn.click === "function") booksBtn.click();
    } else if (nextTab === "library-lectures") {
      const lecBtn = document.querySelector('#lib-master-switcher [data-view="lectures"]');
      if (lecBtn && typeof lecBtn.click === "function") lecBtn.click();
    }

    // Update Workspace Tab Pills (roving tabindex for WAI-ARIA tablist)
    document.querySelectorAll("[data-workspace-tab]").forEach((btn) => {
      const btnTab = btn.getAttribute("data-workspace-tab");
      const isMatch = btnTab === tabId || btnTab === nextTab;
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
        if (nextTab === "about") {
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

    // Mount #tree-majors-block inside dedicated #majors-tab-mount without duplicates
    function syncMajorsMount() {
      const mount = document.getElementById("majors-tab-mount");
      if (!mount) return;
      let block = document.querySelector("#struct-tree-canvas #tree-majors-block") || document.getElementById("tree-majors-block");
      if (!block && typeof window.switchStructureView === "function") {
        try {
          window.switchStructureView("tree");
        } catch (e) { }
        block = document.querySelector("#struct-tree-canvas #tree-majors-block") || document.getElementById("tree-majors-block");
      }
      if (block) {
        if (block.parentElement !== mount || mount.children.length > 1) {
          mount.replaceChildren(block);
        }
      }
    }
    syncMajorsMount();

    requestAnimationFrame(() => {
      revealActiveElements();
      setTimeout(revealActiveElements, 120);

      if (focusAnchor) {
        const target = document.getElementById(focusAnchor);
        if (target) {
          const headerH = (document.getElementById("site-header")?.offsetHeight || 72) + 58;
          const y = target.getBoundingClientRect().top + window.scrollY - headerH;
          window.scrollTo({ top: Math.max(0, y), behavior: "smooth" });
          return;
        }
      }

      if (scrollToTop) {
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

  // Intercept clicks on workspace tabs and in-page section anchors
  document.addEventListener("click", (e) => {
    const tabTrigger = e.target.closest("[data-workspace-tab]");
    if (tabTrigger) {
      // Allow Ctrl/Cmd/Shift/Middle-click to open as a new browser tab natively
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button === 1) return;
      e.preventDefault();
      const targetTab = tabTrigger.getAttribute("data-workspace-tab");
      const focusAnchor = tabTrigger.getAttribute("data-focus-anchor") || null;
      closeMobileDrawerIfOpen();
      setActiveTab(targetTab, { scrollToTop: !focusAnchor, updateUrl: true, pushHistory: true, focusAnchor });
      return;
    }

    const anchor = e.target.closest('a[href^="#"]');
    if (!anchor) return;
    const href = anchor.getAttribute("href");
    if (!href || href === "#") return;
    const targetId = href.slice(1);
    const ownerTab = resolveTabForTarget(targetId);

    // Highlight clicked pill in #desktop-nav when it is an anchor pill
    if (anchor.classList.contains("workspace-tab-btn") && anchor.closest("#desktop-nav")) {
      document.querySelectorAll("#desktop-nav .workspace-tab-btn").forEach((b) => {
        b.classList.toggle("is-active", b === anchor);
      });
    }

    // Special campus floor shortcut anchors (#campus-floor-1 .. #campus-floor-5, #campus-all-floors)
    if (targetId.startsWith("campus-floor-") && typeof window.switchCampusFloor === "function") {
      e.preventDefault();
      closeMobileDrawerIfOpen();
      setActiveTab("campus", { scrollToTop: false, updateUrl: true, focusAnchor: "campus-navigator" });
      window.switchCampusFloor(targetId.replace("campus-floor-", ""));
      return;
    }
    if (targetId === "campus-all-floors" && typeof window.switchCampusFloor === "function") {
      e.preventDefault();
      closeMobileDrawerIfOpen();
      setActiveTab("campus", { scrollToTop: false, updateUrl: true, focusAnchor: "campus-navigator" });
      window.switchCampusFloor("all");
      return;
    }

    // Intercept library vs library-lectures to toggle books / lectures pane
    if (targetId === "library") {
      const booksBtn = document.querySelector('#lib-master-switcher [data-view="books"]');
      if (booksBtn && typeof booksBtn.click === "function") booksBtn.click();
    } else if (targetId === "library-lectures") {
      const lecBtn = document.querySelector('#lib-master-switcher [data-view="lectures"]');
      if (lecBtn && typeof lecBtn.click === "function") lecBtn.click();
    }

    if (ownerTab && activeTab !== "all" && activeTab !== ownerTab) {
      e.preventDefault();
      closeMobileDrawerIfOpen();
      setActiveTab(ownerTab, { scrollToTop: false, updateUrl: true, pushHistory: true, focusAnchor: targetId });
    }
  });

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

  // Wrap cross-section global functions exposed by script.js
  document.addEventListener("DOMContentLoaded", () => {
    if (typeof window.switchStructureView === "function") {
      const origStruct = window.switchStructureView;
      window.switchStructureView = function wrappedSwitchStructureView(view) {
        if (activeTab !== "all" && activeTab !== "structure") {
          setActiveTab("structure", { scrollToTop: false, updateUrl: true });
        }
        return origStruct.apply(this, arguments);
      };
    }

    if (typeof window.switchCampusFloor === "function") {
      const origCampus = window.switchCampusFloor;
      window.switchCampusFloor = function wrappedSwitchCampusFloor(floor) {
        if (activeTab !== "all" && activeTab !== "campus") {
          setActiveTab("campus", { scrollToTop: false, updateUrl: true });
        }
        return origCampus.apply(this, arguments);
      };
    }

    if (typeof window.openLibraryLecturesView === "function") {
      const origLib = window.openLibraryLecturesView;
      window.openLibraryLecturesView = function wrappedOpenLibLectures(fbkFilter) {
        if (activeTab !== "all" && activeTab !== "library" && activeTab !== "library-lectures") {
          setActiveTab("library-lectures", { scrollToTop: false, updateUrl: true });
        }
        return origLib.apply(this, arguments);
      };
    }

    // Trigger tab activation on initial URL query (?tab=...) or #hash
    let initialTab = "about";
    let initialAnchor = null;
    try {
      const params = new URLSearchParams(window.location.search);
      const qTab = params.get("tab");
      if (qTab && VALID_TABS.includes(qTab)) {
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
      if (e.state && e.state.tab && VALID_TABS.includes(e.state.tab)) {
        popTab = e.state.tab;
        popAnchor = e.state.anchor || null;
      } else {
        const params = new URLSearchParams(window.location.search);
        const qTab = params.get("tab");
        if (qTab && VALID_TABS.includes(qTab)) {
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

  // Horizontal wheel glide + fixed dropdown alignment for scrollable #workspace-tabs-bar
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
