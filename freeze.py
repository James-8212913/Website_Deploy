from flask_frozen import Freezer
from app import app

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_404_NOT_FOUND']=True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    ##freezer.run(debug=True)
