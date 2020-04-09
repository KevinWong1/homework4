import markdown
md = markdown.Markdown(extensions=["markdown.extensions.meta"])
data = """title: My New Blog
author: Jane Q Hacker


Welcome to my ~~site~~ *blog*

Paragraphs with *styling* and [a link to Google](http://google.com/)

![And an image](image.jpg)
<h1>And HTML is okay, too</h1>
<div>And HTML is okay, too</div>

"""
html = md.convert(data)
title = md.Meta["title"][0]
author = md.Meta["author"][0]
# print(title, "by", author)
# print(html)

open("test.html","w+").write(html)
