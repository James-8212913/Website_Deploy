import markdown, pygments
from flask import Flask, render_template, render_template_string
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from flask_bootstrap import Bootstrap
from pygments import highlight

# https://dev.to/deadwisdom/embracing-jamstack-with-python-generating-a-static-website-with-flask-and-deploying-to-netlify-4bge
# This has been adopted from the tutorial above

# Tell Flatpages to auto reload when changes are made and look for .md files
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'

# Tell markdown to include the pygment extensions using codehilite, fenced code and tables
def my_markdown(text):
    markdown_text = render_template_string(text)
    pygmented_text = markdown.markdown(markdown_text, extensions = ["codehilite", "fenced_code", "tables"])
    return pygmented_text

# create the opject, use this for our setting as well
app = Flask(__name__)
bootstrap = Bootstrap(app)

# For settings the file itself is used

app.config.from_object(__name__)

# Includes the html renderer for the rendering of the pages

app.config["FLATPAGES_HTML_RENDERER"] = my_markdown

# This stops Flask putting slashes after paths, becuase they get turned into 'flat files'

app.url_map.strict_slashes = False

#Create an instance of our extension
pages = FlatPages(app)

## Route to Flatpages and our root directory in addition to any path that ends in ".html"
@app.route('/')

@app.route("/<path:path>.html")
def page(path=None):
    # Look for the flatpages or find "index" if we have one loaded
    page = pages.get_or_404(path)
     # Render the template "page.html" with our page and title
    return render_template("base.html", page=page, title=page.meta.get('title',''))

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {"Content-Type": "text/css"}
