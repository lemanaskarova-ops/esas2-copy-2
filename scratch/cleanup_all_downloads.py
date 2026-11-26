import re

with open('script.js', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. Update second set of FBK chips (lines 8421-8480)
# Notice style="display:inline-flex; align-items:center; gap:6px; background:rgba(184,147,74,0.18)..."
def replace_fbk_chip_style(m):
    url = m.group(1)
    icon = m.group(2)
    label = m.group(3)
    return f'<button type="button" class="fbk-chip fbk-chip-has-doc" style="display:inline-flex; align-items:center; gap:6px; background:rgba(184,147,74,0.18); border:1px solid var(--gold); color:var(--text); text-decoration:none; padding:6px 14px; border-radius:12px; font-weight:700; cursor:pointer;" title="{label} — Oxu Zalında Aç" onclick="event.stopPropagation(); window.openDocumentReader(\'{url}\', \'{label}\', \'FBK Tədris Vəsaiti\');"><span>{icon} {label}</span><span style="font-size:0.75rem; background:var(--gold); color:#111; padding:2px 6px; border-radius:6px; font-weight:800;">📖 Oxu Zalı</span></button>'

s = re.sub(
    r'<a\s+href="([^"]+)"(?:\s+target="_blank")?\s+download="[^"]*"\s+class="fbk-chip fbk-chip-has-doc"\s+style="[^"]*"\s+title="[^"]*"><span>([^<]*)<\/span><span[^>]*>[^<]*<\/span><\/a>',
    lambda m: f'<button type="button" class="fbk-chip fbk-chip-has-doc" style="display:inline-flex; align-items:center; gap:6px; background:rgba(184,147,74,0.18); border:1px solid var(--gold); color:var(--text); text-decoration:none; padding:6px 14px; border-radius:12px; font-weight:700; cursor:pointer;" onclick="event.stopPropagation(); window.openDocumentReader(\'{m.group(1)}\', \'{m.group(2).strip()}\', \'FBK Tədris Vəsaiti\');"><span>{m.group(2)}</span><span style="font-size:0.75rem; background:var(--gold); color:#111; padding:2px 6px; border-radius:6px; font-weight:800;">📖 Oxu Zalı</span></button>',
    s
)

# 2. Update search catalog item actions in catalog.push
def replace_catalog_download_action(m):
    block = m.group(0)
    # extract href
    href_m = re.search(r'link\.href\s*=\s*"([^"]+)"', block)
    if href_m:
        url = href_m.group(1)
        return f'''action: () => {{
        window.openDocumentReader("{url}", "{url}", "FBK Mühazirələr Fondu");
        const sec = document.getElementById("library");
        sec?.scrollIntoView({{ behavior: "smooth" }});
      }}'''
    return block

s = re.sub(
    r'action:\s*\(\)\s*=>\s*\{\s*const link = document\.createElement\("a"\);[\s\S]*?link\.click\(\);[\s\S]*?\}',
    replace_catalog_download_action,
    s
)

# Also update lines 19075-19086 for books catalog:
old_book_cat_action = """          action: () => {
            if (b.url) {
              const link = document.createElement("a");
              link.href = b.url;
              link.download = b.url.split("/").pop();
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            }
            const sec = document.getElementById("library");
            sec?.scrollIntoView({ behavior: "smooth" });
          }"""

new_book_cat_action = """          action: () => {
            if (b.url) {
              openBookReader(b);
            } else {
              const sec = document.getElementById("library");
              sec?.scrollIntoView({ behavior: "smooth" });
            }
          }"""

s = s.replace(old_book_cat_action, new_book_cat_action)

# Also in openBookReader: remove fallback download button if any
s = s.replace(
    """            <a href="${encodeURI(url)}" download class="btn btn-primary reader-doc-dl-btn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span>${docDlBtn}</span>
            </a>""",
    """            <div class="btn btn-primary reader-doc-dl-btn" style="pointer-events:none; opacity:0.8;">
              <span>📕 Rəqəmsal Oxu Zalı</span>
            </div>"""
)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(s)

print('Updated script.js all downloads cleaned.')
