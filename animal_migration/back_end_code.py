from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/human_migration')
def html_index():
    return render_template('human_migration.html')

@app.route('/animal_migration')
def animal_migration():
    return render_template('my_html_code.html')

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0',)



