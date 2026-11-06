import re

# 1. Load backup majors
with open('/Users/konul/Documents/kollec 2 copy/script.js', 'r', encoding='utf-8') as f:
    backup_content = f.read()

majors_match = re.search(r'majors:\s*\{(?:[^{}]*|\{[^{}]*\})*\}', backup_content, re.DOTALL)
if majors_match:
    full_majors_code = majors_match.group(0)
else:
    print("Majors not found in backup")
    exit()

# 2. Read current script.js
with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Replace majors in staffData
content = re.sub(r'majors:\s*\{.*?\}\s*\}', full_majors_code + "\n  }", content, re.DOTALL)

# 4. Remove initAdmissionCalculator call and function
content = re.sub(r'initAdmissionCalculator\(\);', '', content)
content = re.sub(r'function initAdmissionCalculator\(\) \{.*?\}\s*(?=\/\*|\/\/|\s*const|\s*function)', '', content, re.DOTALL)

# 5. Remove calc_ keys from i18n
content = re.sub(r'calc_.*?: ".*?",\n', '', content)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Majors restored and calculator removed from JS.")
