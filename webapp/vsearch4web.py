from flask import Flask, render_template, request, redirect
from datetime import date
from vsearch import search4letters

app = Flask(__name__)

@app.route('/index')
def index() -> 302:
    return redirect('/entry')

@app.route('/dataatual')
def data_atual() -> str:
    return str(f'Data atual: {date.isoformat(date.today())}')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase, 
                           the_letters=letters,
                           the_title=title, 
                           the_results=results)

@app.route('/')
@app.route('/home')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title=f'Welcome to search4letters on the web! - Data: {date.isoformat(date.today())}')

if __name__ == '__main__':
    app.run(port='5500', debug=True)
