import markdown

with open('equipment-list.md', 'r') as f:
    md_content = f.read()

html_content = markdown.markdown(md_content)

with open('phase1-diagram.drawio.svg', 'r') as f:
    svg_content = f.read()

index_html = f"""
<!DOCTYPE html>
<html>
<head>
  <title>CAMB Sound System</title>
  <style>
    body {{ font-family: sans-serif; }}
    img {{ max-width: 100%; }}
  </style>
</head>
<body>
  <h1>CAMB Sound System</h1>
  <h2>Phase 1 Diagram</h2>
  {svg_content}
  <h2>Equipment List</h2>
  {html_content}
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(index_html)
