#/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/html')
def html_index():
    return "<!doctype html> \
    <html><head><title>HTML Page</title> </head> \
    <body>Hello World</body></html>"

@app.route('/animal')
def animal_migration():
    return "<!doctype html> \
    <html><head><title>Animal Migration</title> </head> \
    <body>Hello World to the Animal Migration</body></html>"

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')


