import datetime
import glob
import os
from jinja2 import Template

def main():
    pages = []
# Auto-discovery of content files
    all_html_files = glob.glob("content/*.html")

    for page in all_html_files:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
            "filename": "content/" + file_name,
            "title": name_only,
            "output": file_name
        })
# Create final pages using content files with jinja2 templating
    year = datetime.datetime.now().strftime('%Y')
    for page in all_html_files:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        content_page = open("content/" + file_name).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        results = template.render(
            title=name_only,
            content=content_page,
            year=str(year),
            pages=pages,
        )
        open("docs/"+file_name,"w+").write(results)

