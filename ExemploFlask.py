from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'pagseguro'

class Jogo:
    def __init__ (self,nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('game1', 'categoria1', 'console1')
jogo2 = Jogo('game2', 'Jogo da galera gente fina mesmo', 'console2')
jogo3 = Jogo('Bauxita atomica de caramelo', 'categoria3', 'Jogo de gente burra mesmo')
lista =[jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template("lista.html", titulo='Jogos', jogos =lista)

@app.route('/novo')
def novo():
    if 'usuario_logado'not in session or session['usuario_logado'] == None:
        return redirect("/login?proxima=novo")
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar ():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect("/")

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash(request.form['usuario'] + ' nao logado! Tente de novo.')
        return redirect('/login')

@app.route("/logout")
def logout():
    session['usuario_logado'] =  None
    flash("Nenhum usuario logado")
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)