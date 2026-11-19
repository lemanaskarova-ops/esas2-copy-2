with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

target_book = '''  {
    id: 45,
    title_az: "Azərbaycan tarixi (Fundamental dərslik, 495 səh.)",
    title_en: "History of Azerbaijan (Comprehensive, 495 p.)",
    title_ru: "История Азербайджана (Фундаментальный учебник, 495 с.)",
    author_az: "Müəllif: Səidə Quliyeva (Humanitar elmlər FBK)",
    author_en: "Author: Saida Guliyeva (Humanities Department)",
    author_ru: "Автор: Саида Гулиева (ФБК Гуманитарных наук)",
    category: "humanitar",
    icon: "🏛️",
    url: "aztarixi2fb.pdf",
  },
'''

assert target_book in content, "target_book not found in script.js"
content = content.replace(target_book, "")

# Also ensure fbk-lec-14 in fbkLecturesArchive is updated with exact Tarix və Humanitar Fənlər and clear 495 səhifə title
lec14_target = '''    // --- Tarix və Hüquq (4) ---
    {
      id: "fbk-lec-14",
      fbkId: "fbk-7",
      fieldBadge: "TARİX VƏ HÜQUQ",
      fieldName_az: "Tarix və Hüquq Elmləri",
      subject_az: "Azərbaycan Tarixi",
      title_az: "Azərbaycan Tarixi Fənnindən Fundamental Mühazirə və Dərs Vəsaiti (495 Səhifə)",
      author_az: "Müəllif: Səidə Quliyeva",'''

lec14_replace = '''    // --- Tarix və Humanitar Fənlər ---
    {
      id: "fbk-lec-14",
      fbkId: "fbk-7",
      fieldBadge: "TARİX VƏ HUMANİTAR",
      fieldName_az: "Tarix və Humanitar Fənlər",
      subject_az: "Azərbaycan Tarixi",
      title_az: "Azərbaycan Tarixi (Fundamental Mühazirə və Dərs Vəsaiti, 495 Səhifə)",
      author_az: "Müəllif: Səidə Quliyeva (Tarix və Humanitar Fənlər FBK)",'''

assert lec14_target in content, "lec14_target not found in script.js"
content = content.replace(lec14_target, lec14_replace)

# Also update lec-15 and lec-16 to TARİX VƏ HUMANİTAR
content = content.replace(
'''    {
      id: "fbk-lec-15",
      fbkId: "fbk-7",
      fieldBadge: "TARİX VƏ HÜQUQ",
      fieldName_az: "Tarix və Hüquq Elmləri",
      subject_az: "Azərbaycan Tarixi (Mühazirə Konspekti)",''',
'''    {
      id: "fbk-lec-15",
      fbkId: "fbk-7",
      fieldBadge: "TARİX VƏ HUMANİTAR",
      fieldName_az: "Tarix və Humanitar Fənlər",
      subject_az: "Azərbaycan Tarixi (Mühazirə Konspekti)",'''
)

content = content.replace(
'''    {
      id: "fbk-lec-16",
      fbkId: "fbk-7",
      fieldBadge: "TARİX VƏ HÜQUQ",
      fieldName_az: "Tarix və Hüquq Elmləri",
      subject_az: "Ümumi Tarix",''',
'''    {
      id: "fbk-lec-16",
      fbkId: "fbk-7",
      fieldBadge: "TARİX VƏ HUMANİTAR",
      fieldName_az: "Tarix və Humanitar Fənlər",
      subject_az: "Ümumi Tarix",'''
)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)

print("script.js successfully updated: id 45 removed from libraryData, fbk-lec-14 refined in fbkLecturesArchive!")
