from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    ##freezer.run(debug=True)

FREEZER_IGNORE_404_NOT_FOUND=True
