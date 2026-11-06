const fs = require('fs');
const path = require('path');

const styleCssPath = '/Users/konul/Documents/esas2 copy 2/style.css';
let css = fs.readFileSync(styleCssPath, 'utf8');

const honorCss = `
/* ═══════════════════════════════════════════════════════════════════════
   FƏXRİ TƏLƏBƏLƏR & ŞƏRƏF LÖVHƏSİ (HALL OF FAME) — ULTRA-PREMIUM STYLES
   ═══════════════════════════════════════════════════════════════════════ */
.grad-honors-wrap {
  position: relative;
  z-index: 2;
  max-width: 1200px;
  margin: 85px auto 0;
  padding: 55px 24px 10px;
  border-top: 1px dashed rgba(207, 169, 94, 0.35);
}

.grad-honors-wrap::before {
  content: "";
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #0a2240;
  border: 2px solid #cfa95e;
  box-shadow: 0 0 15px rgba(207, 169, 94, 0.6);
}

.grad-honors-header {
  text-align: center;
  max-width: 860px;
  margin: 0 auto 40px;
}

.grad-honors-badge-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.grad-honors-kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 7px 18px;
  border-radius: 999px;
  background: rgba(207, 169, 94, 0.16);
  border: 1px solid rgba(207, 169, 94, 0.45);
  color: #f3d792;
  font-size: 0.82rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
}

.grad-honors-kicker svg {
  color: #f3d792;
}

.grad-honors-sub-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(0, 210, 255, 0.12);
  border: 1px solid rgba(0, 210, 255, 0.35);
  color: #7fe4ff;
  font-size: 0.8rem;
  font-weight: 600;
}

.sub-badge-star {
  color: #00d2ff;
  animation: honorPulse 2s infinite ease-in-out;
}

@keyframes honorPulse {
  0%, 100% { transform: scale(1); opacity: 0.8; }
  50% { transform: scale(1.3); opacity: 1; }
}

.grad-honors-title {
  font-family: var(--font-display);
  font-size: clamp(2rem, 3.4vw, 2.75rem);
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 14px;
  line-height: 1.22;
}

.grad-honors-desc {
  font-size: 1.05rem;
  line-height: 1.75;
  color: rgba(248, 250, 252, 0.82);
  margin: 0 auto 30px;
}

.grad-honors-tabs {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(6, 19, 38, 0.85);
  padding: 7px;
  border-radius: 18px;
  border: 1px solid rgba(207, 169, 94, 0.3);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
  flex-wrap: wrap;
  justify-content: center;
}

.honor-tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 12px;
  border: 1px solid transparent;
  background: transparent;
  color: rgba(248, 250, 252, 0.75);
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s ease;
}

.honor-tab-btn:hover {
  color: #ffffff;
  background: rgba(207, 169, 94, 0.15);
}

.honor-tab-btn.active {
  background: linear-gradient(135deg, #cfa95e, #b8934a);
  color: #061326;
  font-weight: 800;
  box-shadow: 0 4px 18px rgba(207, 169, 94, 0.35);
}

.honor-tab-count {
  display: inline-block;
  padding: 2px 7px;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 800;
  background: rgba(255, 255, 255, 0.2);
  color: inherit;
}

.honor-tab-btn.active .honor-tab-count {
  background: #061326;
  color: #cfa95e;
}

/* ═══════════════ HONOR STUDENT CARD ═══════════════ */
.grad-honors-grid {
  display: flex;
  flex-direction: column;
  gap: 36px;
  margin-top: 10px;
}

.honor-student-card {
  position: relative;
  background: linear-gradient(145deg, rgba(11, 32, 60, 0.92) 0%, rgba(6, 19, 38, 0.98) 100%);
  border: 1.5px solid rgba(207, 169, 94, 0.5);
  border-radius: 28px;
  padding: 40px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6), 0 0 50px rgba(207, 169, 94, 0.16);
  backdrop-filter: blur(20px);
  overflow: hidden;
  display: grid;
  grid-template-columns: 310px 1fr;
  gap: 40px;
  align-items: start;
  transition: transform 0.35s ease, box-shadow 0.35s ease;
}

.honor-student-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 32px 75px rgba(0, 0, 0, 0.65), 0 0 65px rgba(207, 169, 94, 0.25);
  border-color: rgba(207, 169, 94, 0.75);
}

.honor-card-ambient {
  position: absolute;
  top: -120px;
  right: -120px;
  width: 380px;
  height: 380px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(207, 169, 94, 0.12), transparent 70%);
  pointer-events: none;
}

/* ASIDE: Avatar, Badges & Quick Action */
.honor-card-aside {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.honor-avatar-wrap {
  position: relative;
  width: 100%;
  max-width: 270px;
  aspect-ratio: 4 / 5;
  border-radius: 22px;
  overflow: hidden;
  border: 2px solid #cfa95e;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.55), 0 0 35px rgba(207, 169, 94, 0.25);
  background: #061326;
  margin-bottom: 18px;
}

.honor-avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 15%;
  transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1);
}

.honor-avatar-wrap:hover .honor-avatar-img {
  transform: scale(1.05);
}

.honor-avatar-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 14px;
  background: linear-gradient(0deg, rgba(6, 19, 38, 0.95) 0%, rgba(6, 19, 38, 0.6) 65%, transparent 100%);
  display: flex;
  justify-content: center;
}

.honor-verified-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 14px;
  border-radius: 999px;
  background: linear-gradient(135deg, #cfa95e, #b8934a);
  color: #061326;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

.honor-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 7px 16px;
  border-radius: 999px;
  background: rgba(16, 185, 129, 0.12);
  border: 1px solid rgba(16, 185, 129, 0.35);
  color: #6ee7b7;
  font-size: 0.82rem;
  font-weight: 700;
  margin-bottom: 20px;
  width: 100%;
  max-width: 270px;
  justify-content: center;
}

.honor-status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
  animation: honorPulse 2s infinite ease-in-out;
}

/* Country Flags Strip */
.honor-flags-box {
  width: 100%;
  max-width: 270px;
  background: rgba(6, 19, 38, 0.6);
  border: 1px solid rgba(207, 169, 94, 0.25);
  border-radius: 16px;
  padding: 14px;
  margin-bottom: 22px;
}

.honor-flags-heading {
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: #cfa95e;
  text-transform: uppercase;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.honor-flags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
}

.honor-flag-tag {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  font-size: 0.78rem;
  font-weight: 600;
  color: #f8fafc;
  transition: all 0.2s ease;
}

.honor-flag-tag:hover {
  background: rgba(207, 169, 94, 0.2);
  border-color: rgba(207, 169, 94, 0.5);
  transform: translateY(-1px);
}

/* Aside Action Buttons */
.honor-aside-actions {
  width: 100%;
  max-width: 270px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.honor-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  padding: 13px 20px;
  border-radius: 14px;
  background: linear-gradient(135deg, #f3d792, #cfa95e, #b8934a);
  color: #061326;
  font-weight: 800;
  font-size: 0.92rem;
  border: none;
  cursor: pointer;
  transition: all 0.28s ease;
  box-shadow: 0 6px 20px rgba(207, 169, 94, 0.35);
  width: 100%;
}

.honor-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(207, 169, 94, 0.5);
  filter: brightness(1.08);
}

.honor-btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px 18px;
  border-radius: 14px;
  background: rgba(207, 169, 94, 0.08);
  border: 1px solid rgba(207, 169, 94, 0.35);
  color: #f3d792;
  font-weight: 700;
  font-size: 0.88rem;
  cursor: pointer;
  transition: all 0.25s ease;
  width: 100%;
}

.honor-btn-secondary:hover {
  background: rgba(207, 169, 94, 0.2);
  border-color: rgba(207, 169, 94, 0.6);
  color: #ffffff;
}

/* MAIN CONTENT AREA */
.honor-card-main {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.honor-main-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.honor-kicker-tag {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 5px 14px;
  border-radius: 999px;
  background: rgba(0, 210, 255, 0.12);
  border: 1px solid rgba(0, 210, 255, 0.35);
  color: #7fe4ff;
  font-size: 0.82rem;
  font-weight: 700;
}

.honor-badge-shimmer {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  border-radius: 999px;
  background: linear-gradient(135deg, rgba(207, 169, 94, 0.25), rgba(207, 169, 94, 0.08));
  border: 1.5px solid #cfa95e;
  color: #fbe3a1;
  font-size: 0.85rem;
  font-weight: 800;
  box-shadow: 0 0 20px rgba(207, 169, 94, 0.3);
  position: relative;
  overflow: hidden;
}

.honor-badge-shimmer::after {
  content: "";
  position: absolute;
  top: 0; left: -100%; width: 50%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  transform: skewX(-20deg);
  animation: honorShine 3.5s infinite;
}

@keyframes honorShine {
  0% { left: -100%; }
  30%, 100% { left: 180%; }
}

.honor-student-name {
  font-family: var(--font-display);
  font-size: clamp(1.8rem, 2.6vw, 2.35rem);
  font-weight: 800;
  color: #ffffff;
  margin: 0;
  line-height: 1.2;
}

.honor-student-role {
  font-size: 1.05rem;
  font-weight: 600;
  color: #cfa95e;
  line-height: 1.5;
  margin-top: -6px;
}

/* 4 Metrics Grid */
.honor-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}

.honor-stat-card {
  background: rgba(6, 19, 38, 0.7);
  border: 1px solid rgba(207, 169, 94, 0.3);
  border-radius: 16px;
  padding: 14px 16px;
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.honor-stat-card:hover {
  background: rgba(10, 32, 60, 0.9);
  border-color: rgba(207, 169, 94, 0.6);
  transform: translateY(-2px);
}

.honor-stat-top {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.honor-stat-icon {
  font-size: 1.25rem;
}

.honor-stat-val {
  font-family: var(--font-display);
  font-size: 1.2rem;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 0.02em;
}

.honor-stat-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: #cfa95e;
  line-height: 1.3;
}

.honor-stat-sub {
  font-size: 0.74rem;
  color: rgba(248, 250, 252, 0.65);
  margin-top: 2px;
}

/* Highlights Box (Recent Milestones) */
.honor-highlights-box {
  background: linear-gradient(135deg, rgba(207, 169, 94, 0.1), rgba(6, 19, 38, 0.75));
  border: 1px solid rgba(207, 169, 94, 0.35);
  border-left: 4px solid #cfa95e;
  border-radius: 18px;
  padding: 18px 22px;
}

.honor-highlights-heading {
  font-size: 0.85rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #f3d792;
  text-transform: uppercase;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.honor-highlights-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.honor-highlight-row {
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-size: 0.92rem;
  line-height: 1.55;
  color: rgba(248, 250, 252, 0.9);
}

.honor-highlight-bullet {
  color: #cfa95e;
  font-size: 0.9rem;
}

.honor-highlight-row strong {
  color: #ffffff;
  font-weight: 700;
}

/* Quote Box */
.honor-quote-box {
  position: relative;
  background: rgba(6, 19, 38, 0.55);
  border-radius: 16px;
  padding: 16px 20px 16px 42px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.honor-quote-icon {
  position: absolute;
  top: 10px;
  left: 14px;
  font-family: var(--font-display);
  font-size: 2.2rem;
  line-height: 1;
  color: #cfa95e;
  opacity: 0.6;
}

.honor-quote-text {
  font-size: 0.92rem;
  line-height: 1.65;
  color: rgba(248, 250, 252, 0.8);
  font-style: italic;
  margin: 0;
}

/* Skill Tags */
.honor-tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.honor-tag-pill {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: rgba(248, 250, 252, 0.85);
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.2s ease;
}

.honor-tag-pill:hover {
  background: rgba(207, 169, 94, 0.2);
  border-color: rgba(207, 169, 94, 0.5);
  color: #ffffff;
}

/* ═══════════════ HONOR STUDENT MODAL ═══════════════ */
.honor-modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: rgba(3, 10, 20, 0.85);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.honor-modal-overlay.open {
  display: flex;
  opacity: 1;
}

.honor-modal-container {
  position: relative;
  width: 100%;
  max-width: 920px;
  max-height: 90vh;
  background: linear-gradient(150deg, #091f38 0%, #051427 100%);
  border: 1.5px solid rgba(207, 169, 94, 0.5);
  border-radius: 26px;
  box-shadow: 0 35px 80px rgba(0, 0, 0, 0.75), 0 0 60px rgba(207, 169, 94, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  animation: honorModalIn 0.32s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes honorModalIn {
  from { opacity: 0; transform: scale(0.92) translateY(20px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

.honor-modal-close {
  position: absolute;
  top: 18px;
  right: 18px;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: rgba(6, 19, 38, 0.8);
  border: 1px solid rgba(207, 169, 94, 0.4);
  color: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: all 0.25s ease;
}

.honor-modal-close:hover {
  background: #cfa95e;
  color: #061326;
  border-color: #cfa95e;
  transform: rotate(90deg);
}

.honor-modal-body {
  overflow-y: auto;
  padding: 36px 40px;
  max-height: calc(90vh - 20px);
}

.honor-modal-hero {
  display: grid;
  grid-template-columns: 140px 1fr;
  gap: 26px;
  align-items: center;
  padding-bottom: 24px;
  border-bottom: 1px solid rgba(207, 169, 94, 0.25);
  margin-bottom: 24px;
}

.honor-modal-avatar {
  width: 140px;
  height: 170px;
  border-radius: 18px;
  object-fit: cover;
  object-position: center 15%;
  border: 2px solid #cfa95e;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
}

.honor-modal-hero-info h3 {
  font-family: var(--font-display);
  font-size: 1.85rem;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 6px;
}

.honor-modal-hero-info p {
  color: #cfa95e;
  font-weight: 600;
  font-size: 1rem;
  margin: 0 0 12px;
}

.honor-modal-hero-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.honor-modal-tab-nav {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  background: rgba(6, 19, 38, 0.7);
  padding: 6px;
  border-radius: 14px;
  border: 1px solid rgba(207, 169, 94, 0.2);
}

.honor-modal-tab {
  flex: 1;
  padding: 10px 16px;
  border-radius: 10px;
  border: none;
  background: transparent;
  color: rgba(248, 250, 252, 0.75);
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: center;
}

.honor-modal-tab:hover {
  color: #ffffff;
  background: rgba(207, 169, 94, 0.12);
}

.honor-modal-tab.active {
  background: #cfa95e;
  color: #061326;
  box-shadow: 0 4px 14px rgba(207, 169, 94, 0.3);
}

.honor-modal-tab-pane {
  display: none;
}

.honor-modal-tab-pane.active {
  display: block;
}

/* Modal Bio Tab */
.honor-modal-bio-p {
  font-size: 0.98rem;
  line-height: 1.8;
  color: rgba(248, 250, 252, 0.88);
  margin-bottom: 16px;
}

/* Modal Timeline Tab */
.honor-modal-timeline {
  position: relative;
  padding-left: 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.honor-modal-timeline::before {
  content: "";
  position: absolute;
  top: 10px;
  bottom: 10px;
  left: 10px;
  width: 2px;
  background: linear-gradient(180deg, #cfa95e, rgba(207, 169, 94, 0.2));
}

.honor-timeline-node {
  position: relative;
}

.honor-timeline-marker {
  position: absolute;
  top: 4px;
  left: -32px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #061326;
  border: 2px solid #cfa95e;
  box-shadow: 0 0 10px rgba(207, 169, 94, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  color: #f3d792;
}

.honor-timeline-content {
  background: rgba(6, 19, 38, 0.6);
  border: 1px solid rgba(207, 169, 94, 0.25);
  border-radius: 14px;
  padding: 16px 20px;
}

.honor-timeline-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 8px;
}

.honor-timeline-year {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 800;
  color: #f3d792;
}

.honor-timeline-badge {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 999px;
  background: rgba(0, 210, 255, 0.12);
  border: 1px solid rgba(0, 210, 255, 0.35);
  color: #7fe4ff;
}

.honor-timeline-title {
  font-size: 1.02rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 6px;
}

.honor-timeline-desc {
  font-size: 0.92rem;
  line-height: 1.65;
  color: rgba(248, 250, 252, 0.8);
  margin: 0;
}

/* Modal Certificates Tab */
.honor-certs-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.honor-cert-item {
  display: flex;
  align-items: center;
  gap: 16px;
  background: rgba(6, 19, 38, 0.65);
  border: 1px solid rgba(207, 169, 94, 0.28);
  border-radius: 16px;
  padding: 16px 18px;
  transition: all 0.25s ease;
}

.honor-cert-item:hover {
  background: rgba(10, 32, 60, 0.85);
  border-color: rgba(207, 169, 94, 0.6);
  transform: translateY(-2px);
}

.honor-cert-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.honor-cert-name {
  font-size: 0.98rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 4px;
}

.honor-cert-org {
  font-size: 0.82rem;
  color: #cfa95e;
  margin: 0;
}

/* Responsive adjustments */
@media (max-width: 960px) {
  .honor-student-card {
    grid-template-columns: 1fr;
    gap: 32px;
    padding: 30px 22px;
  }

  .honor-stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .honor-modal-hero {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .honor-modal-avatar {
    margin: 0 auto;
  }

  .honor-modal-hero-badges {
    justify-content: center;
  }

  .honor-certs-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .honor-stats-grid {
    grid-template-columns: 1fr;
  }

  .honor-modal-body {
    padding: 24px 18px;
  }

  .honor-modal-tab-nav {
    flex-direction: column;
  }
}
`;

if (!css.includes('.grad-honors-wrap')) {
  css += '\n' + honorCss;
  fs.writeFileSync(styleCssPath, css, 'utf8');
  console.log('style.css updated with honor students styles!');
} else {
  console.log('style.css already contains honor students styles.');
}

