import re

html = input()

title_pattern = r"<title>(.*?)</title>"
title_match = re.search(title_pattern, html)
title = title_match.group(1) if title_match else ""

body_pattern = r"<body>(.*?)</body>"
body_match = re.search(body_pattern, html, re.DOTALL)
body_content = body_match.group(1) if body_match else ""

clean_body_content = re.sub(r"<.*?>", "", body_content)

clean_body_content = clean_body_content.replace("\\n", "").strip()

print(f"Title: {title}")
print(f"Content: {clean_body_content}")
