const fs = require("fs");

const scriptPath = "/Users/konul/Documents/esas2 copy 2/script.js";
let script = fs.readFileSync(scriptPath, "utf8");

const originalGalleryCode = `/* ═══════════════ GALLERY MODULE ═══════════════ */
function initGalleryModule() {
  // ─── Data Store: add your images/videos here ───────────────────────
  // type: "image" | "video"
  // src:  path to the file  (relative to index.html)
  // label: short caption shown inside the info bar
  const galleryData = {
    exam: [
      {
        type: "instagram",
        id: "DTPdz9wCPRi",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 1",
      },
      {
        type: "instagram",
        id: "DTPPFBLiHgL",
        postType: "p",
        i18n: "gallery_exam_moment",
        suffix: " - 2",
      },
      {
        type: "instagram",
        id: "DVtLaPLDLWF",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 3",
      },
      {
        type: "instagram",
        id: "DVsUMDqiPY9rcm20_fLGyIBjXu8YEz-Jz4fCZM0",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 4",
      },
      {
        type: "instagram",
        id: "DVtBka2iEe1",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 5",
      },
      {
        type: "instagram",
        id: "DXYt9QPCNf1",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 6",
      }

    ],
    events: [
      {
        type: "instagram",
        id: "DVQe09OCPIJ",
        i18n: "gallery_event_reel",
        suffix: " - 1",
      },
      {
        type: "instagram",
        id: "DVN0zoCCP--",
        i18n: "gallery_event_reel",
        suffix: " - 2",
      },
      {
        type: "instagram",
        id: "DU-Yz-siM5I",
        i18n: "gallery_event_reel",
        suffix: " - 3",
      },
      {
        type: "instagram",
        id: "DU-YmfmCKGP",
        i18n: "gallery_event_reel",
        suffix: " - 4",
      },
      {
        type: "instagram",
        id: "DTu46kkCHYI",
        i18n: "gallery_event_reel",
        suffix: " - 5",
      },
      {
        type: "instagram",
        id: "DWEtsj0CMBQ",
        postType: "reel",
        i18n: "gallery_event_reel",
        suffix: " - 6",
      },
      {
        type: "instagram",
        id: "DViLLrEiBdz",
        postType: "reel",
        i18n: "gallery_event_reel",
        suffix: " - 7",
      },
      {
        type: "instagram",
        id: "DXJtGCoCORp",
        postType: "reel",
        i18n: "gallery_event_reel",
        suffix: " - 8",
      }

    ],
    rooms: [
      {
        type: "instagram",
        id: "DVyqJSNCGt_",
        postType: "reel",
        i18n: "gallery_cat_rooms",
        suffix: " - 1",
      }
    ],
    study: [
      {
        type: "instagram",
        id: "DVtecLDiJMR",
        postType: "reel",
        i18n: "gallery_cat_study",
        suffix: " - 1",
      },
      {
        type: "instagram",
        id: "DVtfSl_iLqE",
        postType: "reel",
        i18n: "gallery_cat_study",
        suffix: " - 2",
      }
    ],
  };

  const catMeta = {
    exam: { icon: "🎓", i18n: "gallery_cat_exam" },
    events: { icon: "🎉", i18n: "gallery_cat_events" },
    rooms: { icon: "🏫", i18n: "gallery_cat_rooms" },
    study: { icon: "📚", i18n: "gallery_cat_study" },
  };

  // ─── DOM refs ────────────────────────────────────────────────────────
  const overlay = document.getElementById("gal-panel-overlay");
  const backdrop = document.getElementById("gal-panel-backdrop");
  const panelBody = document.getElementById("gal-panel-body");
  const panelIcon = document.getElementById("gal-panel-icon");
  const panelTitle = document.getElementById("gal-panel-title");
  const closeBtn = document.getElementById("gal-panel-close");

  const lightbox = document.getElementById("gallery-lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const lightboxClose = document.getElementById("lightbox-close");
  const lightboxBg = document.getElementById("lightbox-backdrop");

  if (!overlay) return;

  // update media counts on cards
  function updateGalleryCounts() {
    const mediaWord =
      currentLang === "ru" ? "медиа" : "media";
    Object.entries(galleryData).forEach(([cat, items]) => {
      const countEl = document.getElementById(\`gal-count-\${cat}\`);
      if (countEl) countEl.textContent = \`\${items.length} \${mediaWord}\`;
    });
  }
  updateGalleryCounts();
  document.addEventListener("languageChanged", updateGalleryCounts);

  // ─── Open / Close Panel ──────────────────────────────────────────────
  function openPanel(cat) {
    const meta = catMeta[cat] || {};
    const items = galleryData[cat] || [];

    // Update header
    if (panelIcon) panelIcon.textContent = meta.icon || "📷";
    if (panelTitle) panelTitle.textContent = gT(meta.i18n || cat);

    // Build media grid
    if (panelBody) {
      if (items.length === 0) {
        const emptyText =
          currentLang === "en"
            ? "No media has been added to this section yet."
            : currentLang === "ru"
              ? "В этот раздел медиафайлы еще не добавлены."
              : "Bu bölmə üçün hələ media əlavə edilməyib.";
        panelBody.innerHTML = \`
          <div class="gal-panel-empty">
            <span class="gal-panel-empty-icon">📂</span>
            <p>\${emptyText}</p>
          </div>\`;
      } else {
        const gridHTML = items.map((item, i) => {
          const delay = \`\${i * 0.07}s\`;

          let label = item.label || "";
          if (item.i18n) {
            label = gT(item.i18n) + (item.suffix || "");
          }

          if (item.type === "instagram") {
            const path = item.postType === "p" ? "p" : "reel";
            return \`
              <div class="gal-media-item gal-media-embed" style="animation-delay:\${delay}">
                <div class="instagram-embed-container">
                  <iframe src="https://www.instagram.com/\${path}/\${item.id}/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
                </div>
                <div class="gal-media-info">
                  <span class="gal-media-label">\${label || "Instagram Post"}</span>
                  <a href="https://www.instagram.com/\${path}/\${item.id}/" target="_blank" class="gal-media-zoom" aria-label="Instagramda bax">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/></svg>
                  </a>
                </div>
              </div>\`;
          }

          if (item.type === "video") {
            return \`
              <div class="gal-media-item" style="animation-delay:\${delay}" data-src="\${item.src}" data-type="video" data-label="\${label}">
                <video src="\${item.src}" muted loop preload="metadata" playsinline></video>
                <span class="gal-video-badge">▶ VIDEO</span>
                <div class="gal-media-info">
                  <span class="gal-media-label">\${label}</span>
                  <button class="gal-media-zoom" aria-label="Böyüt">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                  </button>
                </div>
              </div>\`;
          }
          return \`
            <div class="gal-media-item" style="animation-delay:\${delay}" data-src="\${item.src}" data-type="image" data-label="\${label}">
              <img src="\${item.src}" alt="\${label}" loading="lazy">
              <div class="gal-media-info">
                <span class="gal-media-label">\${label}</span>
                <button class="gal-media-zoom" aria-label="Böyüt">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                </button>
              </div>
            </div>\`;
        }).join("");
        panelBody.innerHTML = \`<div class="gal-media-grid">\${gridHTML}</div>\`;

        // Build lightbox media list (images & videos in this category)
        const viewableItems = [];
        panelBody.querySelectorAll(".gal-media-item:not(.gal-media-embed)").forEach((el, idx) => {
          viewableItems.push({
            src: el.dataset.src,
            label: el.dataset.label || "",
            type: el.dataset.type || "image",
            catTitle: gT(meta.i18n || cat),
          });
          const zoomBtn = el.querySelector(".gal-media-zoom");
          const doOpen = () => openCinemaLightbox(viewableItems, idx);
          el.querySelector("img,video")?.addEventListener("click", doOpen);
          zoomBtn?.addEventListener("click", (e) => {
            e.stopPropagation();
            doOpen();
          });
        });

        // Auto-play videos on hover
        panelBody.querySelectorAll("video").forEach((vid) => {
          vid.closest(".gal-media-item")?.addEventListener("mouseenter", () => vid.play());
          vid.closest(".gal-media-item")?.addEventListener("mouseleave", () => vid.pause());
        });
      }
    }

    overlay.classList.add("active");
    document.documentElement.classList.add("scroll-locked");

    // ── Iris Expand ──────────────────────────────────────
    const ox = overlay._irisX ?? window.innerWidth / 2;
    const oy = overlay._irisY ?? window.innerHeight / 2;
    const r = Math.hypot(
      Math.max(ox, window.innerWidth - ox),
      Math.max(oy, window.innerHeight - oy)
    );
    overlay.style.clipPath = \`circle(0px at \${ox}px \${oy}px)\`;
    overlay.style.transition = 'none';
    void overlay.offsetHeight;
    overlay.style.transition = 'clip-path 0.55s cubic-bezier(0.4, 0, 0.2, 1)';
    overlay.style.clipPath = \`circle(\${r * 1.1}px at \${ox}px \${oy}px)\`;
  }

  function closePanel() {
    const ox = overlay._irisX ?? window.innerWidth / 2;
    const oy = overlay._irisY ?? window.innerHeight / 2;
    const r = Math.hypot(
      Math.max(ox, window.innerWidth - ox),
      Math.max(oy, window.innerHeight - oy)
    );
    overlay.style.transition = 'clip-path 0.45s cubic-bezier(0.4, 0, 0.2, 1)';
    overlay.style.clipPath = \`circle(0px at \${ox}px \${oy}px)\`;
    setTimeout(() => {
      overlay.classList.remove("active");
      overlay.style.clipPath = '';
      overlay.style.transition = '';
      document.documentElement.classList.remove("scroll-locked");
      panelBody?.querySelectorAll("video").forEach((v) => v.pause());
    }, 460);
  }

  // ─── Card Click Listeners ────────────────────────────────────────────
  document.querySelectorAll(".gal-card").forEach((card) => {
    card.addEventListener("click", (e) => {
      const rect = card.getBoundingClientRect();
      overlay._irisX = rect.left + rect.width / 2;
      overlay._irisY = rect.top + rect.height / 2;
      openPanel(card.dataset.panel);
    });
  });

  closeBtn?.addEventListener("click", closePanel);
  backdrop?.addEventListener("click", closePanel);

  // ─── Cinema Lightbox & Fullscreen Slideshow (Upgrade 6) ──────────────
  const lightboxVideo = document.getElementById("lightbox-video");
  const lightboxCounter = document.getElementById("lightbox-counter");
  const lightboxCatPill = document.getElementById("lightbox-cat-pill");
  const lightboxPrev = document.getElementById("lightbox-prev");
  const lightboxNext = document.getElementById("lightbox-next");
  const lightboxThumbs = document.getElementById("lightbox-thumbs");
  const lbSlideshowBtn = document.getElementById("lb-slideshow-btn");
  const lbSlideshowLabel = document.getElementById("lb-slideshow-label");
  const lbZoomBtn = document.getElementById("lb-zoom-btn");

  let lbList = [];
  let lbIndex = 0;
  let lbSlideshowTimer = null;
  let lbZoomed = false;

  function stopSlideshow() {
    if (lbSlideshowTimer) {
      clearInterval(lbSlideshowTimer);
      lbSlideshowTimer = null;
    }
    lbSlideshowBtn?.classList.remove("active");
    if (lbSlideshowLabel) {
      lbSlideshowLabel.textContent =
        currentLang === "en"
          ? "Slideshow"
          : currentLang === "ru"
            ? "Слайд-шоу"
            : "Slayd-Şou";
    }
  }

  function toggleSlideshow() {
    if (lbSlideshowTimer) {
      stopSlideshow();
    } else {
      lbSlideshowBtn?.classList.add("active");
      if (lbSlideshowLabel) {
        lbSlideshowLabel.textContent =
          currentLang === "en"
            ? "Stop"
            : currentLang === "ru"
              ? "Остановить"
              : "Dayandır";
      }
      lbSlideshowTimer = setInterval(() => {
        stepLightbox(1);
      }, 3600);
    }
  }

  function toggleZoom() {
    lbZoomed = !lbZoomed;
    lightboxImg?.classList.toggle("zoomed", lbZoomed);
    lbZoomBtn?.classList.toggle("active", lbZoomed);
  }

  function renderLightboxItem() {
    if (!lightbox || lbList.length === 0) return;
    const item = lbList[lbIndex];
    lbZoomed = false;
    lightboxImg?.classList.remove("zoomed");
    lbZoomBtn?.classList.remove("active");

    if (lightboxImg) {
      lightboxImg.classList.remove("active");
      lightboxImg.src = "";
    }
    if (lightboxVideo) {
      lightboxVideo.classList.remove("active");
      lightboxVideo.pause();
      lightboxVideo.src = "";
    }

    if (item.type === "video") {
      if (lightboxVideo) {
        lightboxVideo.src = item.src;
        lightboxVideo.classList.add("active");
        lightboxVideo.play().catch(() => {});
      }
    } else {
      if (lightboxImg) {
        lightboxImg.src = item.src;
        lightboxImg.alt = item.label || "BDRNK Qalereya";
        lightboxImg.classList.add("active");
      }
    }

    if (lightboxCaption) lightboxCaption.textContent = item.label || "";
    if (lightboxCounter) lightboxCounter.textContent = \`\${lbIndex + 1} / \${lbList.length}\`;
    if (lightboxCatPill) lightboxCatPill.textContent = item.catTitle || "BDRNK Qalereya";

    if (lightboxThumbs) {
      lightboxThumbs.querySelectorAll(".lb-thumb").forEach((t, idx) => {
        t.classList.toggle("active", idx === lbIndex);
      });
      const activeThumb = lightboxThumbs.querySelector(".lb-thumb.active");
      activeThumb?.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    }
  }

  function openCinemaLightbox(list, startIndex = 0) {
    if (!lightbox || !list || list.length === 0) return;
    lbList = list;
    lbIndex = startIndex;
    stopSlideshow();

    if (lightboxThumbs) {
      lightboxThumbs.innerHTML = lbList
        .map((it, idx) => {
          if (it.type === "video") {
            return \`<button type="button" class="lb-thumb \${idx === lbIndex ? "active" : ""}" data-idx="\${idx}" title="\${it.label || "Video"}">
              <span class="lb-thumb-vid">▶</span>
            </button>\`;
          }
          return \`<button type="button" class="lb-thumb \${idx === lbIndex ? "active" : ""}" data-idx="\${idx}" title="\${it.label || ""}">
            <img src="\${it.src}" alt="" loading="lazy" />
          </button>\`;
        })
        .join("");

      lightboxThumbs.querySelectorAll(".lb-thumb").forEach((btn) => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          lbIndex = parseInt(btn.getAttribute("data-idx"), 10) || 0;
          renderLightboxItem();
        });
      });
    }

    renderLightboxItem();
    lightbox.classList.add("active");
  }

  function stepLightbox(dir) {
    if (!lbList.length) return;
    lbIndex = (lbIndex + dir + lbList.length) % lbList.length;
    renderLightboxItem();
  }

  function closeLightbox() {
    stopSlideshow();
    lbZoomed = false;
    lightboxImg?.classList.remove("zoomed");
    lightbox?.classList.remove("active");
    setTimeout(() => {
      if (lightboxImg) lightboxImg.src = "";
      if (lightboxVideo) {
        lightboxVideo.pause();
        lightboxVideo.src = "";
      }
    }, 300);
  }

  lightboxPrev?.addEventListener("click", (e) => {
    e.stopPropagation();
    stepLightbox(-1);
  });
  lightboxNext?.addEventListener("click", (e) => {
    e.stopPropagation();
    stepLightbox(1);
  });
  lbSlideshowBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleSlideshow();
  });
  lbZoomBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleZoom();
  });
  lightboxImg?.addEventListener("dblclick", toggleZoom);

  // Touch swipe support for mobile devices in Cinema Lightbox
  let lbTouchStartX = 0;
  let lbTouchStartY = 0;
  lightbox?.addEventListener(
    "touchstart",
    (e) => {
      if (!e.touches || !e.touches.length) return;
      lbTouchStartX = e.touches[0].clientX;
      lbTouchStartY = e.touches[0].clientY;
    },
    { passive: true },
  );
  lightbox?.addEventListener(
    "touchend",
    (e) => {
      if (!e.changedTouches || !e.changedTouches.length || lbZoomed) return;
      const dx = e.changedTouches[0].clientX - lbTouchStartX;
      const dy = e.changedTouches[0].clientY - lbTouchStartY;
      if (Math.abs(dx) > 48 && Math.abs(dx) > Math.abs(dy) * 1.4) {
        if (dx < 0) stepLightbox(1);
        else stepLightbox(-1);
      }
    },
    { passive: true },
  );

  lightboxClose?.addEventListener("click", closeLightbox);
  lightboxBg?.addEventListener("click", closeLightbox);
  document.addEventListener("keydown", (e) => {
    if (lightbox?.classList.contains("active")) {
      if (e.key === "Escape") closeLightbox();
      else if (e.key === "ArrowRight") stepLightbox(1);
      else if (e.key === "ArrowLeft") stepLightbox(-1);
      else if (e.key === " ") {
        e.preventDefault();
        toggleSlideshow();
      }
    } else if (e.key === "Escape") {
      const readerModal = document.getElementById("book-reader-modal");
      if (readerModal?.classList.contains("active")) {
        readerModal.classList.remove("active");
        document.documentElement.classList.remove("scroll-locked");
      } else if (overlay?.classList.contains("active")) {
        closePanel();
      }
    }
  });
}
`;

const startToken = "/* ═══════════════ GALLERY MODULE";
const endToken = "function initTicker() {";

const startIndex = script.indexOf(startToken);
const endIndex = script.indexOf(endToken);

if (startIndex === -1 || endIndex === -1) {
  console.error("Could not find gallery tokens in script.js!");
  process.exit(1);
}

const revertedScript = script.slice(0, startIndex) + originalGalleryCode + "\n\n" + script.slice(endIndex);
fs.writeFileSync(scriptPath, revertedScript, "utf8");
console.log("Successfully reverted initGalleryModule in script.js!");
