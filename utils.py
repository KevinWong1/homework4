import datetime
import glob
import os
from jinja2 import Template

def main():
    pages = []
# Auto-discovery of content files
    all_content_files = glob.glob("content/*.md")

    for page in all_content_files:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
            "filename": "content/" + file_name,
            "title": name_only,
            "output": file_name
        })
# Create final pages using content files with jinja2 templating
    year = datetime.datetime.now().strftime('%Y')
    for page in all_content_files:
        file_name = os.path.basename(page)
        name_only, extension = os.path.splitext(file_name)
        content_page = open("content/" + file_name).read()
        template_html = open("templates/base.md").read()
        template = Template(template_html)
        results = template.render(
            title=name_only,
            content=content_page,
            year=str(year),
            pages=pages,
        )
        open("docs/"+name_only+".html","w+").write(results)

# Auto-generated blog pages
# NOT WORKING!!
    # blog_pages = []
    # all_blog_posts = glob.glob("blog/*.md")
    
    # for blog in all_blog_posts:
    #     blog_pages.append(open(blog).read())

    # for blog in blog_pages:
    #     file_name = os.path.basename(blog)
    #     template_html = open("templates/blog_base.md").read()
    #     template2 = Template(template_html)
    #     results = template.render(
    #         blog=blog,
    #         year=str(year),
    #     )
    #     open("docs/"+file_name,"w+").write(results)