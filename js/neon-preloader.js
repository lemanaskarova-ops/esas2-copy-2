/**
 * BDRNK Neon "Network Connection" Preloader & Fly-to-Navbar Controller
 * Modular vanilla JS controller with sessionStorage memory, live FLIP geometry,
 * Replay Intro support, click/ESC skip, and prefers-reduced-motion accessibility.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "bdrnk_neon_intro_seen";
  var PROGRESS_DURATION_MS = 1180;
  var PREPARE_EXIT_MS = 1480;
  var FLY_START_MS = 1550;
  var BACKDROP_FADE_MS = 1610;
  var LAND_HANDOFF_MS = 2170;
  var COMPLETE_MS = 2340;
  var WATCHDOG_MS = 3400;

  var preloader = document.getElementById("neon-preloader");
  var flyingLogo = document.getElementById("nn-flying-logo");
  var statusEl = document.getElementById("nn-status");
  var statusTextEl = document.getElementById("nn-status-text");
  var replayBtn = document.getElementById("nn-replay-intro-btn");
  var logoImg = flyingLogo ? flyingLogo.querySelector(".nn-logo-img") : null;

  if (!preloader || !flyingLogo) {
    return;
  }

  var timers = [];
  var rafId = 0;
  var isActive = false;
  var isExiting = false;

  function getTargetLogoEl() {
    return (
      document.getElementById("navbar-logo-target") ||
      document.querySelector('[data-logo-target="true"]') ||
      document.querySelector(".logo-icon")
    );
  }

  function prefersReducedMotion() {
    return (
      typeof window.matchMedia === "function" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    );
  }

  function hasSkipQueryParam() {
    try {
      return new URLSearchParams(window.location.search).get("skipIntro") === "1";
    } catch (e) {
      return false;
    }
  }

  function writeSeenSession() {
    try {
      window.sessionStorage.setItem(STORAGE_KEY, "1");
    } catch (e) {
      // Ignore storage access restrictions
    }
  }

  function clearScheduledWork() {
    for (var i = 0; i < timers.length; i++) {
      window.clearTimeout(timers[i]);
    }
    timers = [];
    if (rafId) {
      window.cancelAnimationFrame(rafId);
      rafId = 0;
    }
  }

  function schedule(fn, delay) {
    var id = window.setTimeout(fn, delay);
    timers.push(id);
    return id;
  }

  // Handle graceful fallback if logo.jpg fails to load
  if (logoImg) {
    logoImg.addEventListener("error", function () {
      flyingLogo.classList.add("nn-svg-fallback");
    });
    if (logoImg.complete && logoImg.naturalWidth === 0) {
      flyingLogo.classList.add("nn-svg-fallback");
    }
  }

  function instantCleanFinish(pulseNavbar) {
    clearScheduledWork();
    isActive = false;
    isExiting = false;

    var docEl = document.documentElement;
    docEl.classList.remove("nn-intro-active");
    docEl.classList.add("nn-skip-intro");

    preloader.classList.remove(
      "nn-running",
      "nn-reduced-replay",
      "is-preparing-exit",
      "is-flying",
      "is-exiting"
    );
    preloader.classList.add("is-hidden");

    var targetEl = getTargetLogoEl();
    if (targetEl) {
      targetEl.classList.remove("nn-logo-incoming");
      if (pulseNavbar && !prefersReducedMotion()) {
        targetEl.classList.remove("nn-landed-pulse");
        void targetEl.offsetWidth;
        targetEl.classList.add("nn-landed-pulse");
      }
    }

    writeSeenSession();
  }

  function performFlyToNavbar() {
    if (!isActive || isExiting) return;
    isExiting = true;

    preloader.classList.add("is-preparing-exit");
    preloader.classList.add("is-flying");

    var targetEl = getTargetLogoEl();
    var startRect = flyingLogo.getBoundingClientRect();
    var targetRect = targetEl ? targetEl.getBoundingClientRect() : null;

    var canLand =
      targetRect &&
      targetRect.width > 0 &&
      targetRect.height > 0 &&
      startRect.width > 0 &&
      targetRect.bottom > 0 &&
      targetRect.top < window.innerHeight;

    if (canLand) {
      var startCenterX = startRect.left + startRect.width / 2;
      var startCenterY = startRect.top + startRect.height / 2;
      var targetCenterX = targetRect.left + targetRect.width / 2;
      var targetCenterY = targetRect.top + targetRect.height / 2;

      var dx = targetCenterX - startCenterX;
      var dy = targetCenterY - startCenterY;
      var scaleX = targetRect.width / startRect.width;
      var scaleY = targetRect.height / startRect.height;
      var scale = (scaleX + scaleY) / 2;

      var computedRadius = parseFloat(window.getComputedStyle(targetEl).borderRadius) || 12;
      var compensatedRadius = (computedRadius / Math.max(scale, 0.2)).toFixed(1) + "px";

      flyingLogo.style.transform =
        "translate3d(" + dx.toFixed(2) + "px, " + dy.toFixed(2) + "px, 0) scale(" + scale.toFixed(4) + ")";
      flyingLogo.style.borderRadius = compensatedRadius;
    } else {
      flyingLogo.style.transform = "translate3d(0, -16px, 0) scale(0.78)";
      flyingLogo.style.opacity = "0";
    }

    schedule(function () {
      preloader.classList.add("is-exiting");
    }, Math.max(0, BACKDROP_FADE_MS - FLY_START_MS));

    schedule(function () {
      if (targetEl) {
        targetEl.classList.remove("nn-logo-incoming");
        targetEl.classList.remove("nn-landed-pulse");
        void targetEl.offsetWidth;
        targetEl.classList.add("nn-landed-pulse");
      }
      flyingLogo.style.opacity = "0";
    }, Math.max(0, LAND_HANDOFF_MS - FLY_START_MS));

    schedule(function () {
      instantCleanFinish(false);
    }, Math.max(0, COMPLETE_MS - FLY_START_MS));
  }

  function startTelemetryCounter() {
    var startTime = performance.now();

    function step(now) {
      if (!isActive || isExiting) return;
      var elapsed = now - startTime;
      var ratio = Math.min(1, elapsed / PROGRESS_DURATION_MS);
      // Smooth ease-out curve for telemetry counter
      var eased = 1 - Math.pow(1 - ratio, 2.2);
      var pct = Math.min(100, Math.round(eased * 100));

      if (statusTextEl) {
        statusTextEl.textContent = pct + "%";
      }

      if (ratio < 1) {
        rafId = window.requestAnimationFrame(step);
      } else {
        if (statusEl) statusEl.classList.add("is-connected");
        if (statusTextEl) statusTextEl.textContent = "100%";
      }
    }

    rafId = window.requestAnimationFrame(step);
  }

  function play(isReplay) {
    clearScheduledWork();
    isActive = true;
    isExiting = false;

    var docEl = document.documentElement;
    docEl.classList.remove("nn-skip-intro");
    docEl.classList.add("nn-intro-active");

    if (prefersReducedMotion()) {
      if (!isReplay) {
        instantCleanFinish(false);
        return;
      }
      // Clean static 280ms crossfade for explicit reduced-motion replay
      preloader.classList.remove("is-hidden", "is-exiting", "is-flying", "is-preparing-exit");
      preloader.classList.add("nn-reduced-replay");
      if (statusEl) statusEl.classList.add("is-connected");
      if (statusTextEl) statusTextEl.textContent = "100%";

      schedule(function () {
        preloader.classList.add("is-exiting");
      }, 280);
      schedule(function () {
        instantCleanFinish(false);
      }, 560);
      return;
    }

    var targetEl = getTargetLogoEl();
    if (targetEl) {
      targetEl.classList.remove("nn-landed-pulse");
      targetEl.classList.add("nn-logo-incoming");
    }

    // Reset state & inline styles before restarting CSS keyframes
    preloader.classList.remove(
      "is-hidden",
      "nn-running",
      "nn-reduced-replay",
      "is-preparing-exit",
      "is-flying",
      "is-exiting"
    );
    flyingLogo.style.transform = "translate3d(0, 0, 0) scale(1)";
    flyingLogo.style.borderRadius = "50%";
    flyingLogo.style.opacity = "1";

    if (statusEl) statusEl.classList.remove("is-connected");
    if (statusTextEl) statusTextEl.textContent = "0%";

    // Force reflow so all SVG & word animations restart from t=0 cleanly
    void preloader.offsetWidth;
    preloader.classList.add("nn-running");

    startTelemetryCounter();

    schedule(function () {
      if (isActive && !isExiting) {
        preloader.classList.add("is-preparing-exit");
      }
    }, PREPARE_EXIT_MS);

    schedule(function () {
      performFlyToNavbar();
    }, FLY_START_MS);

    // Failsafe watchdog if browser tab throttles timers
    schedule(function () {
      if (isActive) {
        instantCleanFinish(false);
      }
    }, WATCHDOG_MS);
  }

  function skip() {
    if (!isActive) return;
    clearScheduledWork();
    if (prefersReducedMotion()) {
      instantCleanFinish(false);
      return;
    }
    if (!isExiting) {
      if (statusEl) statusEl.classList.add("is-connected");
      if (statusTextEl) statusTextEl.textContent = "100%";
      performFlyToNavbar();
    } else {
      instantCleanFinish(false);
    }
  }

  function replay() {
    play(true);
  }

  // Click or Escape to skip cleanly
  preloader.addEventListener("click", skip);
  document.addEventListener("keydown", function (e) {
    if (isActive && e.key === "Escape") {
      skip();
    }
  });

  if (replayBtn) {
    replayBtn.addEventListener("click", function (e) {
      e.preventDefault();
      replay();
    });
  }

  // Auto-play on every page open/reload unless reduced-motion or ?skipIntro=1
  if (prefersReducedMotion() || hasSkipQueryParam()) {
    instantCleanFinish(false);
  } else {
    play(false);
  }

  window.BDRNKNeonPreloader = {
    play: function () {
      play(false);
    },
    replay: replay,
    skip: skip
  };
})();
