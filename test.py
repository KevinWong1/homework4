import glob
all_html_files = glob.glob("content/*.html")
# print(all_html_files)
# ['content\\about.html', 'content\\index.html', 'content\\projects.html'] 

import os
file_path = "content/blog.html"
file_name = os.path.basename(file_path)
# print(file_name)
# prints out blog.html
name_only, extension = os.path.splitext(file_name)
# print(name_only)
# prints out blog

from jinja2 import Template
index_html = open("content/index.html").read()
template_html = open("templates/base.html").read()
template = Template(template_html)
template.render(
title="Homepage",
content=index_html,
)
