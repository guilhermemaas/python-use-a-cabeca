from flask import Flask, render_template, request, redirect, escape
from datetime import date
from vsearch import search4letters
import mysql.connector
from DBcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = { 'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB',
                }

def log_request_old(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        #print(str(dir(req)), res, file=log) -> retorna todas as propriedades e metodos de um objeto
        escape(print(f'Dados Enviados: {req.form}',f'IP Addr: {req.remote_addr}',f'Navegador: {req.user_agent}',
              f'Resultado: {res}', file=log, sep='|'))
       #print('<br>', file=log)


def log_request_old2(req: 'flask_request', res: str) -> None:
    """Detalhes de log das requisicoes web a seus resultados
    Obs.: Inutilizado"""
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
    (phrase, letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res))
    conn.commit()
    cursor.close()
    conn.close()
    
       
def log_request(req: 'flask_request', res: str) -> None:
    """Detalhes de log das requisicoes web a seus resultados"""
    dbconfig = { 'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB',
                }
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
        (phrase, letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res))
        
    
@app.route('/index')
def index() -> 302:
    return redirect('/entry')


@app.route('/dataatual')
def data_atual() -> str:
    return str(f'Data atual: {date.isoformat(date.today())}')


@app.route('/search4', methods=['POST'])
def search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
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

    
@app.route('/viewlogold')
def view_log_old() -> str:
    with open('vsearch.log', 'r') as log:
        contents = log.read()
    return contents


@app.route('/viewlog')
def view_log() -> str:
    contents = []
    with open('vsearch.log', 'r') as log:
        line = escape(log.read())
        contents.append(line.split('|'))
    return str(contents)


@app.route('/viewlog2')
def view_log2() -> 'html':
    contents = []
    with open('vsearch.log', 'r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles= ('Dados Enviados', 'IP addr', 'Navegador', 'Resultados')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents)
    

@app.route('/viewlog3')
def view_log3() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results
        from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Frase', 'Letras', 'Endereco IP', 'Navegador', 'Resultados')
    return render_template('viewlog.html',
                           the_title='Visualizar Log:',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(port='5500', debug=True)
