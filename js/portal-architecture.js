/**
 * BDRNK Official Portal — Clean Architecture Namespace & Runtime API
 * Exposes `window.BDRNK` with lazy dataset getters, Workspace Tab controls,
 * theme/i18n helpers, and live DOM/module diagnostics.
 */
(function (global) {
  "use strict";

  function safeReadGlobal(getter, fallback) {
    try {
      const val = getter();
      return val !== undefined ? val : fallback;
    } catch (_e) {
      return fallback;
    }
  }

  function getActiveTabId() {
    const activeBtn = document.querySelector(".workspace-tab-btn.is-active[data-workspace-tab]");
    if (activeBtn) {
      return activeBtn.getAttribute("data-workspace-tab") || "home";
    }
    try {
      const q = new URLSearchParams(global.location.search).get("tab");
      if (q) return q;
    } catch (_e) {}
    return "home";
  }

  function getThemeMode() {
    const root = document.documentElement;
    return root.classList.contains("dark-mode") || root.classList.contains("dark")
      ? "dark"
      : "light";
  }

  function setThemeMode(mode) {
    const isDark = mode === "dark";
    const root = document.documentElement;
    root.classList.toggle("dark-mode", isDark);
    root.classList.toggle("dark", isDark);
    root.setAttribute("data-theme", isDark ? "dark" : "light");
    if (document.body) {
      document.body.classList.toggle("dark", isDark);
    }
    try {
      global.localStorage.setItem("bdrnk-theme", isDark ? "dark" : "light");
    } catch (_e) {}
    return isDark ? "dark" : "light";
  }

  const BDRNK = {
    version: "2.0.0",

    tabs: {
      switch: function (tabId, options) {
        if (typeof global.switchWorkspaceTab === "function") {
          global.switchWorkspaceTab(tabId, options || { scrollToTop: true, updateUrl: true, pushHistory: true });
          return true;
        }
        return false;
      },
      getActive: getActiveTabId,
      list: function () {
        return Array.from(document.querySelectorAll(".workspace-tab-btn[data-workspace-tab]"))
          .map(function (el) { return el.getAttribute("data-workspace-tab"); })
          .filter(Boolean);
      },
      openStructureView: function (view) {
        return typeof global.switchStructureView === "function"
          ? (global.switchStructureView(view), true)
          : false;
      },
      openCampusFloor: function (floor) {
        return typeof global.switchCampusFloor === "function"
          ? (global.switchCampusFloor(floor), true)
          : false;
      },
      openLibraryLectures: function (fbkFilter) {
        return typeof global.openLibraryLecturesView === "function"
          ? (global.openLibraryLecturesView(fbkFilter), true)
          : false;
      },
    },

    theme: {
      get: getThemeMode,
      set: setThemeMode,
      toggle: function () {
        const toggleBtn = document.getElementById("theme-toggle");
        if (toggleBtn) {
          toggleBtn.click();
          return getThemeMode();
        }
        return setThemeMode(getThemeMode() === "dark" ? "light" : "dark");
      },
    },

    i18n: {
      getLang: function () {
        try {
          return (
            document.documentElement.lang ||
            global.localStorage.getItem("bdrnk_lang") ||
            "az"
          );
        } catch (_e) {
          return document.documentElement.lang || "az";
        }
      },
      setLang: function (lang) {
        const btn = document.querySelector('.lang-btn[data-lang="' + lang + '"]');
        if (btn) {
          btn.click();
          return true;
        }
        return false;
      },
      t: function (key) {
        return safeReadGlobal(function () {
          return typeof gT === "function" ? gT(key) : "";
        }, "");
      },
    },

    data: {
      get news() {
        return safeReadGlobal(function () { return typeof newsData !== "undefined" ? newsData : []; }, []);
      },
      get library() {
        return safeReadGlobal(function () { return typeof libraryData !== "undefined" ? libraryData : []; }, []);
      },
      get lectures() {
        return safeReadGlobal(function () { return typeof lecturesData !== "undefined" ? lecturesData : []; }, []);
      },
      get fbkLectures() {
        return safeReadGlobal(function () { return typeof fbkLecturesArchive !== "undefined" ? fbkLecturesArchive : (global.__bdrnkFbkLectures || []); }, []);
      },
      get scienceAuthors() {
        return safeReadGlobal(function () { return typeof scienceAuthorsData !== "undefined" ? scienceAuthorsData : (global.__bdrnkScienceAuthors || []); }, []);
      },
      get teacherCertificates() {
        return safeReadGlobal(function () { return typeof teacherCertificatesData !== "undefined" ? teacherCertificatesData : []; }, []);
      },
      get certificates() {
        return safeReadGlobal(function () { return typeof certificatesData !== "undefined" ? certificatesData : (global.__bdrnkCertificates || []); }, []);
      },
      get honorStudents() {
        return safeReadGlobal(function () { return typeof honorStudentsData !== "undefined" ? honorStudentsData : (global.__bdrnkHonorStudents || []); }, []);
      },
      get faq() {
        return safeReadGlobal(function () { return typeof faqData !== "undefined" ? faqData : []; }, []);
      },
      get campusRooms() {
        return global.CAMPUS_ROOMS || [];
      },
    },

    diagnostics: function () {
      const idCounts = Object.create(null);
      let duplicateIds = 0;
      document.querySelectorAll("[id]").forEach(function (el) {
        const id = el.id;
        idCounts[id] = (idCounts[id] || 0) + 1;
        if (idCounts[id] === 2) duplicateIds += 1;
      });

      const panels = document.querySelectorAll("[data-tab-panel]");
      const activePanels = document.querySelectorAll("[data-tab-panel].is-active");
      const stylesheets = Array.from(document.querySelectorAll('link[rel="stylesheet"]'))
        .map(function (lnk) { return lnk.getAttribute("href"); })
        .filter(Boolean);

      return {
        version: BDRNK.version,
        activeTab: getActiveTabId(),
        theme: getThemeMode(),
        lang: BDRNK.i18n.getLang(),
        panelCount: panels.length,
        activePanelCount: activePanels.length,
        i18nNodes: document.querySelectorAll("[data-i18n]").length,
        duplicateIds: duplicateIds,
        stylesheets: stylesheets,
        counts: {
          news: BDRNK.data.news.length,
          library: BDRNK.data.library.length,
          lectures: BDRNK.data.lectures.length,
          fbkLectures: BDRNK.data.fbkLectures.length,
          scienceAuthors: BDRNK.data.scienceAuthors.length,
          teacherCertificates: BDRNK.data.teacherCertificates.length,
          certificates: BDRNK.data.certificates.length,
          honorStudents: BDRNK.data.honorStudents.length,
          faq: BDRNK.data.faq.length,
        },
      };
    },
  };

  Object.defineProperty(global, "BDRNK", {
    value: Object.freeze(BDRNK),
    writable: false,
    configurable: false,
  });
})(window);
