from flask import Flask, render_templates 

app = Flask(__name__)

@app.route('/')
def index():
    return render_templates('home.html')

@app.route('/human')
def html_index():
    return render_templates('human_migration')

@app.route('/animal')
def animal_migration():
    return render_templates('my_html_code.html')

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')


