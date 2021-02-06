#############################################################################
# Program:
#    Lab 02 Python Web Server, Computer Networks
#    Brother Jones, CSE354
# Author:
#    Whitney LeSueur
# Summary:
#    This program will launch a webserver using the flask module and return
#    The text and images of a given HTML file.
#
##############################################################################

# To be run via command line...

# Import flask module
from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

# Default to index, which is a copy of bufbomb.html
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')