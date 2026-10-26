from flask import Flask, render_template_string, request
import json
from pathlib import Path

app = Flask(__name__)

# Caminho do arquivo de usuários
ARQUIVO_USUARIOS = Path(__file__).parent / "usuarios.json"


def carregar_usuarios():
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


HTML_TELA = '''
<form method="POST">
    <h2>Login</h2>

    <input type="text" name="usuario"
           placeholder="Usuário" required>
    <br><br>

    <input type="password" name="senha"
           placeholder="Senha" required>
    <br><br>

    <button type="submit">Entrar</button>
</form>
'''


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        usuarios = carregar_usuarios()

        if usuario in usuarios and usuarios[usuario] == senha:
            return f"<h1>Sucesso! Bem-vindo, {usuario}.</h1>"

        return '''
            <h1>Falha! Usuário ou senha incorretos.</h1>
            <a href="/">Tentar de novo</a>
        '''

    return render_template_string(HTML_TELA)


if __name__ == "__main__":
    app.run(debug=True)