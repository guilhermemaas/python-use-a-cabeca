from flask import Flask
from datetime import date
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/dataatual')
def data_atual() -> str:
    return f'Data atual: {date.isoformat(date.today())}'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everithing!', 'aeiru,!'))

app.run(port='5500')