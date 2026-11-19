import re
import json

# ========================================================
# 1. APPEND CSS TO style.css
# ========================================================
css_code = '''
/* ══════════════════════════════════════════════════════════════
   OFFICIAL COLLEGE TEXTBOOKS & STUDY GUIDES REGISTRY (2025/2026 - 2026/2027)
══════════════════════════════════════════════════════════════ */
.science-textbooks-registry {
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

.science-tb-header-wrap {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.science-tb-kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono, monospace);
  font-size: 0.74rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--gold, #b8934a);
  background: rgba(184, 147, 74, 0.12);
  border: 1px solid rgba(184, 147, 74, 0.3);
  padding: 4px 12px;
  border-radius: 999px;
  width: fit-content;
}

.science-tb-title {
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--text, #0f172a);
  margin: 0;
  line-height: 1.3;
}

.science-tb-desc {
  font-size: 0.92rem;
  color: var(--text-dim, #64748b);
  margin: 0;
  line-height: 1.6;
}

.science-tb-stat-strip {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

@media (min-width: 768px) {
  .science-tb-stat-strip {
    grid-template-columns: repeat(4, 1fr);
  }
}

.science-tb-stat-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 14px;
  background: var(--surface-2, rgba(15, 23, 42, 0.04));
  border: 1px solid var(--border, rgba(15, 23, 42, 0.08));
}

.science-tb-stat-icon {
  font-size: 1.5rem;
  line-height: 1;
}

.science-tb-stat-val {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text, #0f172a);
}

.science-tb-stat-lbl {
  font-size: 0.75rem;
  color: var(--text-dim, #64748b);
  font-weight: 600;
}

.science-tb-controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  padding: 10px 16px;
  border-radius: 14px;
  background: var(--surface-2, rgba(15, 23, 42, 0.03));
  border: 1px solid var(--border, rgba(15, 23, 42, 0.06));
}

.science-tb-filters {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.science-tb-filter-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 999px;
  border: 1px solid var(--border, rgba(15, 23, 42, 0.1));
  background: var(--surface, #ffffff);
  color: var(--text-secondary, #475569);
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}

.science-tb-filter-btn:hover {
  border-color: var(--gold, #b8934a);
  color: var(--text, #0f172a);
}

.science-tb-filter-btn.active {
  background: #0a2240;
  color: #ffffff;
  border-color: #0a2240;
}

.dark .science-tb-filter-btn.active {
  background: var(--gold, #b8934a);
  color: #061529;
  border-color: var(--gold, #b8934a);
}

.science-tb-cards-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 640px) {
  .science-tb-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .science-tb-cards-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.science-tb-card {
  display: flex;
  flex-direction: column;
  padding: 18px;
  border-radius: 18px;
  background: var(--surface, #ffffff);
  border: 1px solid var(--border, rgba(15, 23, 42, 0.08));
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
  position: relative;
  transition: all 0.25s ease;
}

.science-tb-card:hover {
  transform: translateY(-3px);
  border-color: var(--gold, #b8934a);
  box-shadow: 0 10px 24px rgba(184, 147, 74, 0.12);
}

.science-tb-card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 12px;
}

.science-tb-type-pill {
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 3px 8px;
  border-radius: 6px;
}

.science-tb-type-pill.type-derslik {
  background: rgba(37, 99, 235, 0.1);
  color: #2563eb;
  border: 1px solid rgba(37, 99, 235, 0.25);
}

.dark .science-tb-type-pill.type-derslik {
  background: rgba(96, 165, 250, 0.15);
  color: #93c5fd;
  border-color: rgba(96, 165, 250, 0.3);
}

.science-tb-type-pill.type-vesait {
  background: rgba(16, 185, 129, 0.1);
  color: #059669;
  border: 1px solid rgba(16, 185, 129, 0.25);
}

.dark .science-tb-type-pill.type-vesait {
  background: rgba(52, 211, 153, 0.15);
  color: #6ee7b7;
  border-color: rgba(52, 211, 153, 0.3);
}

.science-tb-year-badge {
  font-family: var(--font-mono, monospace);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-dim, #64748b);
  background: var(--surface-2, rgba(15, 23, 42, 0.04));
  padding: 2px 6px;
  border-radius: 4px;
}

.science-tb-book-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--text, #0f172a);
  margin: 0 0 8px;
  line-height: 1.35;
}

.science-tb-qrif-row {
  margin-bottom: 12px;
}

.science-tb-qrif-tag {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: var(--font-mono, monospace);
  font-size: 0.72rem;
  font-weight: 700;
  background: rgba(184, 147, 74, 0.1);
  color: var(--gold, #b8934a);
  border: 1px dashed rgba(184, 147, 74, 0.35);
  padding: 3px 8px;
  border-radius: 6px;
  word-break: break-all;
}

.science-tb-authors {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text, #0f172a);
  margin-bottom: 4px;
}

.science-tb-roles {
  font-size: 0.76rem;
  color: var(--text-dim, #64748b);
  line-height: 1.45;
  margin-bottom: 12px;
  flex: 1;
}

.science-tb-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 10px;
  border-top: 1px solid var(--border, rgba(15, 23, 42, 0.06));
  font-size: 0.74rem;
  color: var(--text-dim, #64748b);
  font-weight: 600;
}

/* Official Table for Textbooks */
.science-tb-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.84rem;
  min-width: 800px;
}

.science-tb-table th {
  background: var(--surface-2, rgba(15, 23, 42, 0.05));
  color: var(--text, #0f172a);
  padding: 12px 14px;
  text-align: left;
  font-weight: 800;
  border-bottom: 2px solid var(--border, rgba(15, 23, 42, 0.1));
}

.science-tb-table td {
  padding: 12px 14px;
  border-bottom: 1px solid var(--border, rgba(15, 23, 42, 0.06));
  color: var(--text-secondary, #334155);
}

.science-tb-table tbody tr:hover {
  background: rgba(184, 147, 74, 0.04);
}
'''

with open("style.css", "r", encoding="utf-8") as f:
    style_content = f.read()

if "science-textbooks-registry" not in style_content:
    style_content += "\n" + css_code
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(style_content)
    print("style.css updated with textbooks registry styles!")

print("Step 1 done.")
