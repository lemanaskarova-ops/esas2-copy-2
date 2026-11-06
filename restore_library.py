import re

# Read data from the backup file
with open('/Users/konul/Documents/kollec 2 copy/script.js', 'r', encoding='utf-8') as f:
    backup_content = f.read()

# Extract libraryData and lecturesData
lib_match = re.search(r'const libraryData = \[.*?\];', backup_content, re.DOTALL)
lec_match = re.search(r'const lecturesData = \[.*?\];', backup_content, re.DOTALL)

if not lib_match or not lec_match:
    print("Could not find libraryData or lecturesData in backup")
    exit()

library_code = lib_match.group(0)
lectures_code = lec_match.group(0)

# Read current script.js
with open('script.js', 'r', encoding='utf-8') as f:
    current_content = f.read()

# Find where to insert (before lecturesData or after newsData)
insert_pos = re.search(r'const lecturesData = \[', current_content)
if not insert_pos:
    # If lecturesData is also missing or weird, try after newsData
    insert_pos = re.search(r'const newsData = \[.*?\];', current_content, re.DOTALL)
    if insert_pos:
        # Insert after newsData
        new_content = current_content[:insert_pos.end()] + "\n\n" + library_code + "\n\n" + lectures_code + current_content[insert_pos.end():]
    else:
        print("Could not find insertion point")
        exit()
else:
    # Replace lecturesData and insert libraryData before it
    # We find the end of lecturesData to replace it entirely with the backup version
    lec_end = re.search(r'const lecturesData = \[.*?\];', current_content, re.DOTALL)
    if lec_end:
        new_content = current_content[:insert_pos.start()] + library_code + "\n\n" + lectures_code + "\n\n" + current_content[lec_end.end():]
    else:
        new_content = current_content[:insert_pos.start()] + library_code + "\n\n" + lectures_code + "\n\n" + current_content[insert_pos.start():]

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Library and Lectures data restored successfully")
