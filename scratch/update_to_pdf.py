import re
import unicodedata
import os

with open('script.js', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. Update i18n search chips and bento
s = s.replace('search_chip_edebiyyat: "📖 Ədəbiyyat (edebiyyatfb.docx)"', 'search_chip_edebiyyat: "📖 Ədəbiyyat (edebiyyatfb.pdf)"')
s = s.replace('search_chip_tarix: "🏛️ Azərbaycan Tarixi (aztarixifb.docx)"', 'search_chip_tarix: "🏛️ Azərbaycan Tarixi (aztarixifb.pdf)"')
s = s.replace('search_chip_edebiyyat: "📖 Literature (edebiyyatfb.docx)"', 'search_chip_edebiyyat: "📖 Literature (edebiyyatfb.pdf)"')
s = s.replace('search_chip_tarix: "🏛️ History of Azerbaijan (aztarixifb.docx)"', 'search_chip_tarix: "🏛️ History of Azerbaijan (aztarixifb.pdf)"')
s = s.replace('search_chip_edebiyyat: "📖 Литература (edebiyyatfb.docx)"', 'search_chip_edebiyyat: "📖 Литература (edebiyyatfb.pdf)"')
s = s.replace('search_chip_tarix: "🏛️ История Азербайджана (aztarixifb.docx)"', 'search_chip_tarix: "🏛️ История Азербайджана (aztarixifb.pdf)"')

s = s.replace('bento_2_d: "Dərsliklər, DOCX/PDF mühazirə fondu və rəqəmsal oxu zalı"', 'bento_2_d: "Dərsliklər, PDF mühazirə fondu və rəqəmsal oxu zalı"')
s = s.replace('bento_2_d: "Textbooks, DOCX/PDF lecture archive and digital reading room"', 'bento_2_d: "Textbooks, PDF lecture archive and digital reading room"')
s = s.replace('bento_2_d: "Учебники, архив лекций DOCX/PDF и цифровой читальный зал"', 'bento_2_d: "Учебники, архив лекций PDF и цифровой читальный зал"')

# 2. Update libraryData books (lines 6010-6950)
# We can find all url: "...docx" and replace with corresponding pdf
def replace_library_url(match):
    full_url = match.group(1)
    # Don't touch if already .docx.pdf
    if full_url.endswith('.docx.pdf'):
        return f'url: "{full_url}"'
    base = full_url[:-5] if full_url.endswith('.docx') else full_url
    # find corresponding pdf on disk
    pdf_cand = base + '.pdf'
    # Check normalized
    for f in os.listdir('.'):
        if unicodedata.normalize('NFC', f) == unicodedata.normalize('NFC', pdf_cand):
            return f'url: "{f}"'
    # Fallback to direct replace
    return f'url: "{base}.pdf"'

s = re.sub(r'url:\s*"([^"]+\.docx)"', replace_library_url, s)

# 3. Update fbkLecturesArchive format: "docx" -> format: "pdf"
# Also volume and fileSize in lecturesData
s = s.replace('volume: "Geniş Konspekt · DOCX"', 'volume: "Geniş Konspekt · PDF"')
s = s.replace('fileSize: "5.3 MB DOCX"', 'fileSize: "5.3 MB PDF"')

s = s.replace('volume: "Yenilənmiş Vəsait · DOCX"', 'volume: "Yenilənmiş Vəsait · PDF"')
s = s.replace('fileSize: "DOCX Vəsait"', 'fileSize: "PDF Vəsait"')

s = s.replace('volume: "Mühazirələr Toplusu (2023) · DOCX"', 'volume: "Mühazirələr Toplusu (2023) · PDF"')
s = s.replace('fileSize: "2.7 MB DOCX"', 'fileSize: "2.7 MB PDF"')

s = s.replace('volume: "52 Стр. · Курс Лекций · DOCX"', 'volume: "52 Стр. · Курс Лекций · PDF"')
s = s.replace('fileSize: "130 KB DOCX"', 'fileSize: "130 KB PDF"')

s = s.replace('volume: "Mühazirələr Toplusu · DOCX"', 'volume: "Mühazirələr Toplusu · PDF"')
s = s.replace('fileSize: "80 KB DOCX"', 'fileSize: "80 KB PDF"')

s = s.replace('fileSize: "DOCX Konspekt"', 'fileSize: "PDF Konspekt"')

s = s.replace('title_az: "Azərbaycan Tarixi Fənnindən Mühazirələr Toplusu (72 Saat · DOCX Konspekt)"', 'title_az: "Azərbaycan Tarixi Fənnindən Mühazirələr Toplusu (72 Saat · Mühazirə Konspekti)"')
s = s.replace('volume: "72 Saat · Word Nəşri"', 'volume: "72 Saat · PDF Nəşri"')
s = s.replace('redaktə edilə bilən Word (DOCX) nəşri', 'rəsmi PDF nəşri')

s = s.replace('extraDocUrl: "aztarixifb.docx"', 'extraDocUrl: "aztarixifb.pdf"')

s = s.replace('volume: "Mühazirələr Konspekti · DOCX"', 'volume: "Mühazirələr Konspekti · PDF"')
s = s.replace('fileSize: "180 KB DOCX"', 'fileSize: "180 KB PDF"')

s = s.replace('volume: "Курс Лекций · DOCX"', 'volume: "Курс Лекций · PDF"')
s = s.replace('fileSize: "238 KB DOCX"', 'fileSize: "238 KB PDF"')

s = s.replace('fileSize: "82 KB DOCX"', 'fileSize: "82 KB PDF"')
s = s.replace('fileSize: "97 KB DOCX"', 'fileSize: "97 KB PDF"')

s = s.replace('volume: "Курс Лекций · 16 Стр. · DOCX"', 'volume: "Курс Лекций · 16 Стр. · PDF"')
s = s.replace('fileSize: "81 KB DOCX"', 'fileSize: "81 KB PDF"')

s = s.replace('fileSize: "126 KB DOCX"', 'fileSize: "126 KB PDF"')

s = s.replace('volume: "Курс Лекций (2023) · DOCX"', 'volume: "Курс Лекций (2023) · PDF"')
s = s.replace('fileSize: "185 KB DOCX"', 'fileSize: "185 KB PDF"')

s = s.replace('fileSize: "1.2 MB DOCX"', 'fileSize: "1.2 MB PDF"')
s = s.replace('fileSize: "173 KB DOCX"', 'fileSize: "173 KB PDF"')
s = s.replace('fileSize: "356 KB DOCX"', 'fileSize: "356 KB PDF"')

s = s.replace('volume: "57 Стр. · Курс Лекций · DOCX"', 'volume: "57 Стр. · Курс Лекций · PDF"')
s = s.replace('fileSize: "436 KB DOCX"', 'fileSize: "436 KB PDF"')

s = s.replace('fileSize: "119 KB DOCX"', 'fileSize: "119 KB PDF"')
s = s.replace('fileSize: "197 KB DOCX"', 'fileSize: "197 KB PDF"')

# Update format: "docx" to format: "pdf"
s = s.replace('format: "docx"', 'format: "pdf"')

# 4. FBK Chips and drawer replacements
chips_map = [
    ('azdilifb.docx', 'azdilifb.pdf'),
    ('edebiyyatfb.docx', 'edebiyyatfb.pdf'),
    ('KOMMUNİKASİYA DF 2 (1).docx', 'KOMMUNİKASİYA DF 2 (1).pdf'),
    ('umtarixfb.docx', 'umtarixfb.pdf'),
    ('yeni mühazirələr.docx', 'yeni mühazirələr.pdf'),
    ('yeni mühazirələr.docx', 'yeni mühazirələr.pdf'),
    ('1Русский язык 1 курс (лекции) (1).docx', '1Русский язык 1 курс (лекции) (1).pdf'),
    ('2Русский язык 2 курс лекции книга  (1).docx', '2Русский язык 2 курс лекции книга  (1).pdf'),
    ('aztarixifb.docx', 'aztarixifb.pdf'),
]

for old_name, new_name in chips_map:
    s = s.replace(f'href="{old_name}"', f'href="{new_name}"')
    s = s.replace(f'download="{old_name}"', f'download="{new_name}"')
    s = s.replace(f'link.href = "{old_name}"', f'link.href = "{new_name}"')
    s = s.replace(f'link.download = "{old_name}"', f'link.download = "{new_name}"')
    s = s.replace(f'({old_name})', f'({new_name})')
    s = s.replace(f'title="{old_name} —', f'title="{new_name} —')
    s = s.replace(f'Yüklə: {old_name}', f'Yüklə: {new_name}')

s = s.replace('<span>azdilifb.docx Faylını Yüklə</span>', '<span>azdilifb.pdf Faylını Aç / Yüklə</span>')
s = s.replace('<span>edebiyyatfb.docx Faylını Yüklə</span>', '<span>edebiyyatfb.pdf Faylını Aç / Yüklə</span>')
s = s.replace('<span>Kommunikasiya Mühazirəsini Yüklə (DOCX)</span>', '<span>Kommunikasiya Mühazirəsini Aç / Yüklə (PDF)</span>')
s = s.replace('<span>aztarixifb.docx (DOCX)</span>', '<span>aztarixifb.pdf (PDF)</span>')
s = s.replace('<span>umtarixfb.docx Faylını Yüklə</span>', '<span>umtarixfb.pdf Faylını Aç / Yüklə</span>')
s = s.replace('<span>yeni mühazirələr.docx Faylını Yüklə</span>', '<span>yeni mühazirələr.pdf Faylını Aç / Yüklə</span>')
s = s.replace('<span>Rus Dili I Kurs Mühazirə Yüklə (DOCX)</span>', '<span>Rus Dili I Kurs Mühazirəni Aç / Yüklə (PDF)</span>')
s = s.replace('<span>Rus Dili II Kurs Mühazirə Kitabı Yüklə (DOCX)</span>', '<span>Rus Dili II Kurs Mühazirə Kitabını Aç / Yüklə (PDF)</span>')

s = s.replace('📥 DOCX', '📥 PDF')
s = s.replace('📥 2 DOCX', '📥 2 PDF')
s = s.replace('📥 PDF + DOCX', '📥 PDF')
s = s.replace('PDF & DOCX', 'PDF')

# Badges and catalog
s = s.replace('badge: "DOCX • Mühazirə"', 'badge: "PDF • Mühazirə"')
s = s.replace('badge: "DOCX • 25k+ Söz"', 'badge: "PDF • 25k+ Söz"')
s = s.replace('tokens: "azdilifb azdili docx', 'tokens: "azdilifb azdili pdf')
s = s.replace('tokens: "edebiyyatfb docx', 'tokens: "edebiyyatfb pdf')
s = s.replace('tokens: "aztarixifb docx', 'tokens: "aztarixifb pdf')
s = s.replace('tokens: "umtarixfb docx', 'tokens: "umtarixfb pdf')
s = s.replace('tokens: "yeni muhazireler yeni mühazirələr docx', 'tokens: "yeni muhazireler yeni mühazirələr pdf')
s = s.replace('fbk 06 docx derslik', 'fbk 06 pdf derslik')

# In quick search modal
s = s.replace('data-i18n="search_chip_edebiyyat">📖 Ədəbiyyat (edebiyyatfb.docx)</button>', 'data-i18n="search_chip_edebiyyat">📖 Ədəbiyyat (edebiyyatfb.pdf)</button>')
s = s.replace('data-i18n="search_chip_tarix">🏛️ Azərbaycan Tarixi (aztarixifb.docx)</button>', 'data-i18n="search_chip_tarix">🏛️ Azərbaycan Tarixi (aztarixifb.pdf)</button>')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(s)

print('Updated script.js successfully.')

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

h = h.replace('data-i18n="search_chip_edebiyyat">📖 Ədəbiyyat (edebiyyatfb.docx)</button>', 'data-i18n="search_chip_edebiyyat">📖 Ədəbiyyat (edebiyyatfb.pdf)</button>')
h = h.replace('data-i18n="search_chip_tarix">🏛️ Azərbaycan Tarixi (aztarixifb.docx)</button>', 'data-i18n="search_chip_tarix">🏛️ Azərbaycan Tarixi (aztarixifb.pdf)</button>')

with open('index.html', 'w', encoding='utf-8') as f:
    h = f.write(h)

print('Updated index.html successfully.')
