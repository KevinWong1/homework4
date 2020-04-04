import datetime
import glob
import os

# array of files in content dir


y = datetime.datetime.now().strftime('%Y')

def main():
    pages = []
# Phase 1 - Auto-discovery of content files
    all_html_files = glob.glob("content/*.html")

    for page in all_html_files:
        file_name = os.path.basename(page)
        print(file_name)
        name_only, extension = os.path.splitext(file_name)
        print(name_only, extension)
        pages.append({
            "filename": "content/" + file_name,
            "title": name_only,
            "output": "docs/" + file_name
        })
    print(pages)

    for page in pages:
        almost_finished_page = apply_template(page['filename'])
        almost_almost_finished_page = almost_finished_page.replace('{{year}}', str(y))
        finished_page = almost_almost_finished_page.replace("{{title}}", page['title'])

        if (page['title'] == 'Blog'):
            x = finished_page.replace('{{blog_nav_class}}', 'active')
        elif(page['title'] == 'About Me'):
            x = finished_page.replace('{{about_nav_class}}', 'active')
        else:
            x = finished_page.replace('{{project_nav_class}}', 'active')

        output_file(page['output'], x)

    blog_posts = [
        {
        "filename": "blog/1.html",
        "date": "September 3rd, 2018",
        "title": "My experience so far as a noob at Kickstart Coding",
        },
        {
        "filename": "blog/2.html",
        "date": "September 10th, 2018",
        "title": "So far I really like Ubuntu Linux",
        },
        {
        "filename": "blog/3.html",
        "date": "September 15th, 2018",
        "title": "My thoughts on Python so far",
        },
        ]
    for blog in blog_posts:
        template = open("./templates/base.html").read()
        finished_page = template.replace("{{content}}", blog['title'])
        output_file(blog['filename'], finished_page)
        
def apply_template(content_location):
    # Read in template
    template = open("./templates/base.html").read()
    # store "real content" to a variable
    real_content = (open(content_location).read())
    # string replacing
    finished_page = template.replace("{{content}}", real_content)
    return finished_page

def output_file(destination, page):
    open(destination, 'w+').write(page)

main()
