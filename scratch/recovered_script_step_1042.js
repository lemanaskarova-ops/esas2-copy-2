const fs = require("fs");
const path = require("path");

const scriptPath = "/Users/konul/Documents/esas2 copy 2/script.js";
let script = fs.readFileSync(scriptPath, "utf8");

const enriched = JSON.parse(fs.readFileSync("/tmp/enriched_gallery.json", "utf8"));

// Build the new gallery implementation code
const newGalleryCode = `/* ═══════════════ GALLERY MODULE (UPGRADE: CONCEPTS 1, 2, 7 & 3) ═══════════════ */
function initGalleryModule() {
  // Institutional Campus Photo Collection (50 High-Res Real Photos categorized)
  const campusPhotos = ${JSON.stringify(enriched, null, 2)};

  // Category Meta
  const catMeta = {
    exam: { icon: "🎓", i18n: "gallery_cat_exam", fallback: "İmtahan və Nailiyyətlər" },
    events: { icon: "🎉", i18n: "gallery_cat_events", fallback: "Tədbirlər" },
    rooms: { icon: "🏫", i18n: "gallery_cat_rooms", fallback: "Auditoriyalar" },
    study: { icon: "📚", i18n: "gallery_cat_study", fallback: "Dərs Mühiti" },
  };

  // Group photos by category
  const galleryData = {
    exam: campusPhotos.filter((p) => p.cat === "exam"),
    events: campusPhotos.filter((p) => p.cat === "events"),
    rooms: campusPhotos.filter((p) => p.cat === "rooms"),
    study: campusPhotos.filter((p) => p.cat === "study"),
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
  const lightboxVideo = document.getElementById("lightbox-video");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const lightboxDate = document.getElementById("lightbox-date");
  const lightboxTag = document.getElementById("lightbox-tag");
  const lightboxCounter = document.getElementById("lightbox-counter");
  const lightboxCatPill = document.getElementById("lightbox-cat-pill");
  const lightboxPrev = document.getElementById("lightbox-prev");
  const lightboxNext = document.getElementById("lightbox-next");
  const lightboxThumbs = document.getElementById("lightbox-thumbs");
  const lbSlideshowBtn = document.getElementById("lb-slideshow-btn");
  const lbSlideshowLabel = document.getElementById("lb-slideshow-label");
  const lbZoomBtn = document.getElementById("lb-zoom-btn");
  const lbShareBtn = document.getElementById("lb-share-btn");
  const lightboxClose = document.getElementById("lightbox-close");
  const lightboxBg = document.getElementById("lightbox-backdrop");

  const mosaicGrid = document.getElementById("gal-mosaic-grid");
  const mosaicFilterWrap = document.getElementById("gal-mosaic-filters");
  const mosaicMoreBtn = document.getElementById("gal-mosaic-more-btn");

  let currentMosaicFilter = "all";
  let mosaicVisibleCount = 12;

  // ─── Update Card Counts ──────────────────────────────────────────────
  function updateGalleryCounts() {
    const photoWord = currentLang === "en" ? "photos" : currentLang === "ru" ? "фото" : "foto";
    Object.entries(galleryData).forEach(([cat, items]) => {
      const countEl = document.getElementById(\`gal-count-\${cat}\`);
      if (countEl) countEl.textContent = \`\${items.length} \${photoWord}\`;
      const filterCountEl = document.getElementById(\`gal-filter-count-\${cat}\`);
      if (filterCountEl) filterCountEl.textContent = items.length;
    });
    const filterAllCount = document.getElementById("gal-filter-count-all");
    if (filterAllCount) filterAllCount.textContent = campusPhotos.length;
  }
  updateGalleryCounts();
  document.addEventListener("languageChanged", () => {
    updateGalleryCounts();
    renderMosaic();
  });

  // ─── Concept 2: Live Background Photo Cycling on Category Cards ─────
  function initCardBackgroundCycling() {
    const cardBgMap = {
      exam: galleryData.exam.slice(0, 6).map((p) => p.src),
      events: galleryData.events.slice(0, 6).map((p) => p.src),
      rooms: galleryData.rooms.slice(0, 6).map((p) => p.src),
      study: galleryData.study.slice(0, 6).map((p) => p.src),
    };

    document.querySelectorAll(".gal-card").forEach((card) => {
      const cat = card.dataset.panel;
      const images = cardBgMap[cat] || [];
      const bgEl = card.querySelector(".gal-card-bg");
      if (!bgEl || images.length <= 1) return;

      let idx = 0;
      let interval = null;

      // Subtle cycling on hover
      card.addEventListener("mouseenter", () => {
        interval = setInterval(() => {
          idx = (idx + 1) % images.length;
          bgEl.style.backgroundImage = \`url('\${images[idx]}')\`;
        }, 1600);
      });

      card.addEventListener("mouseleave", () => {
        if (interval) {
          clearInterval(interval);
          interval = null;
        }
      });
    });
  }
  initCardBackgroundCycling();

  // ─── Concept 1: Live Interactive Photo Mosaic ─────────────────────────
  function getPhotoTitle(photo) {
    if (!photo) return "";
    return photo[\`title_\${currentLang}\`] || photo.title_az || "";
  }
  function getPhotoDate(photo) {
    if (!photo) return "";
    return photo[\`date_\${currentLang}\`] || photo.date_az || "";
  }
  function getPhotoTag(photo) {
    if (!photo) return "";
    return photo[\`tag_\${currentLang}\`] || photo.tag_az || "";
  }

  function getFilteredPhotos() {
    if (currentMosaicFilter === "all") return campusPhotos;
    return campusPhotos.filter((p) => p.cat === currentMosaicFilter);
  }

  function renderMosaic() {
    if (!mosaicGrid) return;
    const filtered = getFilteredPhotos();
    const toShow = filtered.slice(0, mosaicVisibleCount);

    if (toShow.length === 0) {
      mosaicGrid.innerHTML = \`<div class="gal-panel-empty"><p>Foto tapılmadı.</p></div>\`;
      if (mosaicMoreBtn) mosaicMoreBtn.style.display = "none";
      return;
    }

    mosaicGrid.innerHTML = toShow
      .map((photo, i) => {
        const title = getPhotoTitle(photo);
        const date = getPhotoDate(photo);
        const tag = getPhotoTag(photo);
        const catInfo = catMeta[photo.cat] || {};
        const catLabel = gT(catInfo.i18n) || catInfo.fallback || photo.cat;

        // Visual rhythm: every 5th item spans 2 rows
        const isSpanned = i % 7 === 0 || i % 7 === 4 ? "gal-mosaic-tall" : "";

        return \`
          <div class="gal-mosaic-item \${isSpanned}" data-photo-id="\${photo.id}" style="animation-delay: \${(i % 12) * 0.04}s">
            <img src="\${photo.src}" alt="\${title}" loading="lazy" />
            <div class="gal-mosaic-overlay">
              <div class="gal-mosaic-badges">
                <span class="gal-mosaic-cat">\${catInfo.icon || "📷"} \${catLabel}</span>
                \${tag ? \`<span class="gal-mosaic-tag">\${tag}</span>\` : ""}
              </div>
              <h4 class="gal-mosaic-title">\${title}</h4>
              <div class="gal-mosaic-footer">
                \${date ? \`<span class="gal-mosaic-date">📅 \${date}</span>\` : ""}
                <span class="gal-mosaic-zoom-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                </span>
              </div>
            </div>
          </div>
        \`;
      })
      .join("");

    // Click on mosaic item to open in Cinema Lightbox
    mosaicGrid.querySelectorAll(".gal-mosaic-item").forEach((itemEl, idx) => {
      itemEl.addEventListener("click", () => {
        const currentFiltered = getFilteredPhotos();
        const lbItems = currentFiltered.map((p) => ({
          type: "image",
          src: p.src,
          label: getPhotoTitle(p),
          date: getPhotoDate(p),
          tag: getPhotoTag(p),
          catTitle: (catMeta[p.cat] ? gT(catMeta[p.cat].i18n) : "") || "BDRNK Qalereya",
        }));
        openCinemaLightbox(lbItems, idx);
      });
    });

    if (mosaicMoreBtn) {
      mosaicMoreBtn.style.display = mosaicVisibleCount >= filtered.length ? "none" : "inline-flex";
    }
  }

  // Filter Buttons
  if (mosaicFilterWrap) {
    mosaicFilterWrap.addEventListener("click", (e) => {
      const btn = e.target.closest(".gal-filter-pill");
      if (!btn) return;
      mosaicFilterWrap.querySelectorAll(".gal-filter-pill").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentMosaicFilter = btn.dataset.filter || "all";
      mosaicVisibleCount = 12;
      renderMosaic();
    });
  }

  // Load More Button
  if (mosaicMoreBtn) {
    mosaicMoreBtn.addEventListener("click", () => {
      mosaicVisibleCount += 12;
      renderMosaic();
    });
  }

  // Initial mosaic render
  renderMosaic();

  // ─── Concept 3: Video Filmstrip Card Interactive Playback ─────────────
  document.querySelectorAll(".gal-filmstrip-card").forEach((card) => {
    const video = card.querySelector("video");
    const playBtn = card.querySelector(".gal-film-play-btn");
    const src = card.dataset.videoSrc;

    // Hover preview
    if (video) {
      card.addEventListener("mouseenter", () => {
        video.play().catch(() => {});
      });
      card.addEventListener("mouseleave", () => {
        video.pause();
      });
    }

    // Click opens video directly in Cinema Lightbox
    card.addEventListener("click", () => {
      const title =
        currentLang === "en"
          ? card.dataset.videoTitleEn
          : currentLang === "ru"
            ? card.dataset.videoTitleRu
            : card.dataset.videoTitle;
      const lbVideoItem = [
        {
          type: "video",
          src: src,
          label: title || "BDRNK Video İcmal",
          date: "BDRNK Rəqəmsal Media",
          tag: "HD Video",
          catTitle: "Video İcmal",
        },
      ];
      openCinemaLightbox(lbVideoItem, 0);
    });
  });

  // ─── Open / Close Category Overlay Panel ─────────────────────────────
  function openPanel(cat) {
    const meta = catMeta[cat] || {};
    const items = galleryData[cat] || [];

    if (panelIcon) panelIcon.textContent = meta.icon || "📷";
    if (panelTitle) panelTitle.textContent = gT(meta.i18n) || meta.fallback || cat;

    if (panelBody) {
      if (items.length === 0) {
        panelBody.innerHTML = \`
          <div class="gal-panel-empty">
            <span class="gal-panel-empty-icon">📂</span>
            <p>\${currentLang === "en" ? "No photos available." : currentLang === "ru" ? "Фотографии отсутствуют." : "Foto tapılmadı."}</p>
          </div>\`;
      } else {
        const gridHTML = items
          .map((item, i) => {
            const title = getPhotoTitle(item);
            const date = getPhotoDate(item);
            const tag = getPhotoTag(item);
            return \`
              <div class="gal-media-item" style="animation-delay:\${i * 0.04}s" data-idx="\${i}">
                <img src="\${item.src}" alt="\${title}" loading="lazy">
                <div class="gal-media-info">
                  <span class="gal-media-label">\${title}</span>
                  <button class="gal-media-zoom" aria-label="Böyüt">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                  </button>
                </div>
              </div>\`;
          })
          .join("");

        panelBody.innerHTML = \`<div class="gal-media-grid">\${gridHTML}</div>\`;

        // Click to open in Cinema Lightbox
        const lbItems = items.map((p) => ({
          type: "image",
          src: p.src,
          label: getPhotoTitle(p),
          date: getPhotoDate(p),
          tag: getPhotoTag(p),
          catTitle: gT(meta.i18n) || meta.fallback,
        }));

        panelBody.querySelectorAll(".gal-media-item").forEach((el, idx) => {
          el.addEventListener("click", () => openCinemaLightbox(lbItems, idx));
        });
      }
    }

    overlay.classList.add("active");
    document.documentElement.classList.add("scroll-locked");

    const ox = overlay._irisX ?? window.innerWidth / 2;
    const oy = overlay._irisY ?? window.innerHeight / 2;
    const r = Math.hypot(Math.max(ox, window.innerWidth - ox), Math.max(oy, window.innerHeight - oy));
    overlay.style.clipPath = \`circle(0px at \${ox}px \${oy}px)\`;
    overlay.style.transition = "none";
    void overlay.offsetHeight;
    overlay.style.transition = "clip-path 0.55s cubic-bezier(0.4, 0, 0.2, 1)";
    overlay.style.clipPath = \`circle(\${r * 1.1}px at \${ox}px \${oy}px)\`;
  }

  function closePanel() {
    const ox = overlay._irisX ?? window.innerWidth / 2;
    const oy = overlay._irisY ?? window.innerHeight / 2;
    overlay.style.transition = "clip-path 0.45s cubic-bezier(0.4, 0, 0.2, 1)";
    overlay.style.clipPath = \`circle(0px at \${ox}px \${oy}px)\`;
    setTimeout(() => {
      overlay.classList.remove("active");
      overlay.style.clipPath = "";
      overlay.style.transition = "";
      document.documentElement.classList.remove("scroll-locked");
    }, 460);
  }

  // Card click triggers category panel
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

  // ─── Concept 7: Upgraded Cinema Lightbox with Captions & Share ───────
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
      lbSlideshowLabel.textContent = gT("lb_slideshow") || "Slayd-Şou";
    }
  }

  function toggleSlideshow() {
    if (lbSlideshowTimer) {
      stopSlideshow();
    } else {
      lbSlideshowBtn?.classList.add("active");
      if (lbSlideshowLabel) {
        lbSlideshowLabel.textContent = gT("lb_stop") || "Dayandır";
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

  function shareCurrentMedia() {
    const item = lbList[lbIndex];
    if (!item) return;
    const shareTitle = item.label || "BDRNK Foto Qalereya";
    const shareUrl = window.location.href.split("#")[0] + "#gallery";

    if (navigator.share) {
      navigator
        .share({
          title: shareTitle,
          text: \`BDRNK Qalereya: \${shareTitle}\`,
          url: shareUrl,
        })
        .catch(() => {});
    } else if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(shareUrl).then(() => {
        const btnText = lbShareBtn.querySelector("span");
        const orig = btnText ? btnText.textContent : "";
        if (btnText) btnText.textContent = currentLang === "en" ? "Copied!" : "Kopyalandı!";
        setTimeout(() => {
          if (btnText) btnText.textContent = orig;
        }, 2000);
      });
    }
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
    if (lightboxDate) lightboxDate.textContent = item.date ? \`📅 \${item.date}\` : "";
    if (lightboxTag) lightboxTag.textContent = item.tag ? \`🏷️ \${item.tag}\` : "";
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
  lbShareBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    shareCurrentMedia();
  });
  lightboxImg?.addEventListener("dblclick", toggleZoom);

  // Mobile Swipe for Lightbox
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

// Replace initGalleryModule in script.js
const startToken = "/* ═══════════════ GALLERY MODULE ═══════════════ */";
const endToken = "function initTicker() {";

const startIndex = script.indexOf(startToken);
const endIndex = script.indexOf(endToken);

if (startIndex === -1 || endIndex === -1) {
  console.error("Could not find gallery tokens in script.js!");
  process.exit(1);
}

const updatedScript = script.slice(0, startIndex) + newGalleryCode + "\n\n" + script.slice(endIndex);
fs.writeFileSync(scriptPath, updatedScript, "utf8");
console.log("Successfully updated initGalleryModule in script.js!");
