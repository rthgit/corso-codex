import re
import os

with open('e:/Corso Codex/openai_codex_corso_definitivo_con_community.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<img class="hero-logo" src="(data:image/png;base64,[^"]+)">', text)
logo_src = match.group(1) if match else "logo.png"

parts = []
for i in range(19):
    with open(f'e:/Corso Codex/part_{i}.html', 'r', encoding='utf-8') as f:
        parts.append(f.read())

full_html = "".join(parts)
# The split might have removed the separator <section class="page-break"> because split() consumes it.
# Wait, my split logic was: parts = text.split('<section class="page-break">')
# So I need to join them WITH the separator, EXCEPT for part 0 which is the header.

full_html = parts[0]
for part in parts[1:]:
    full_html += '<section class="page-break">' + part

# Restore logo
full_html = full_html.replace('src="logo.png"', f'src="{logo_src}"')

with open('e:/Corso Codex/openai_codex_corso_definitivo_con_community_en.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Assembled successfully")
