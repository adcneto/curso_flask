from flask import Flask, render_template, request, redirect

app = Flask(__name__)


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
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        return redirect("/") 
    else:
        return redirect('/login')

app.run(debug=True)