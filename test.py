# import glob
# all_html_files = glob.glob("content/*.html")
# print(all_html_files)
# # ['content\\about.html', 'content\\index.html', 'content\\projects.html'] 

# import os
# file_path = "content/blog.html"
# # file_path = all_html_files[0]
# file_name = os.path.basename(file_path)
# print(file_name)
# # prints out blog.html
# name_only, extension = os.path.splitext(file_name)
# print(name_only)
# # prints out blog



from jinja2 import Template
index_html = open("content/index.html").read()
template_html = open("templates/base.html").read()
template = Template(template_html)
results = template.render(
title="Homepage",
content=index_html,
)
print('printing index_html')
print(index_html)
print('____________________')
print('printing template_html')
print(template_html)
print('____________________')
print('printing rendered')
print(results)

# template = Template("""
#     <h1>hi {{ name }}!</h1>
#     <p>Age: {{ age }}</p>
# """)
# result = template.render(
#     name="Joaquin",
#     age=37,
# )
# print(result)
