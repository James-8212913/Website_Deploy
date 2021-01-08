from flask import Flask, render_template
from flask_flatpages import FlatPages

# https://dev.to/deadwisdom/embracing-jamstack-with-python-generating-a-static-website-with-flask-and-deploying-to-netlify-4bge
# This has been adopted from the tutorial above

# Tell Flatpages to auto reload when changes are made and look for .md files
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'

# create the opject, use this for our setting as well
app = Flask(__name__)

# For settings the file itself is used

app.config.from_object(__name__)

# This stops Flask putting slashes after paths, becuase they get turned into 'flat files'

app.url_map.strict_slashes = False

#Create an instance of our extension
pages = FlatPages(app)

## Route to Flatpages and our root directory in addition to any path that ends in ".html"
@app.route("/")
@app.route("/<path:path>.html")
def page(path=None):
    # Look for the flatpages or find "index" if we have one loaded
    page = pages.get_or_404(path or 'index')
     # Render the template "page.html" with our page and title
    return render_template("page.html", page=page, title=page.meta.get('title', ''))