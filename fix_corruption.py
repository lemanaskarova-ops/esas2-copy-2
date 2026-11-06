import re

# Read clean news data
with open('news_data_js.txt', 'r', encoding='utf-8') as f:
    clean_news_code = f.read()

# Read script.js
with open('script.js', 'r', encoding='utf-8', errors='ignore') as f:
    script_content = f.read()

# Find the start of corrupted newsData
# It starts around 'const newsData = ['
# And we want to replace until 'const lecturesData = ['
start_pattern = r'const newsData = \['
end_pattern = r'const lecturesData = \['

match_start = re.search(start_pattern, script_content)
match_end = re.search(end_pattern, script_content)

if match_start and match_end:
    new_content = script_content[:match_start.start()] + clean_news_code + "\n\n" + script_content[match_end.start():]
    
    # Also fix some common corruption patterns if they exist outside that block
    # Like ]; followed by characters on the same line
    new_content = re.sub(r'\];[A-Za-z0-9_"]+.*?\n', '];\n', new_content)
    
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replacement successful")
else:
    print(f"Could not find patterns: Start={bool(match_start)}, End={bool(match_end)}")
