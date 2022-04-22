from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    lists = [
        {'id': 1, 'name': 'List to Bideronka'},
        {'id': 2, 'name': 'List to Lidl'},
        {'id': 3, 'name': 'List to Żabka'}
    ]
    return render_template('home.html', lists=lists)

@app.route('/about')
def about_page():
    return render_template('about.html')