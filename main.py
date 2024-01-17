# 1.) criar paginas HTML
# 2.) route -> treinamentos.com (qual link irá abrir cada página)
# 3.) função -> def home() é o que você quer exibir naquela página
# 4.) executa o site -> app.run()
# 5.) Publicar o site na Internet

# depois de instalado o FLASK dentro do Visual Studio Code, agora está importando a biblioteca;
# FLASK é a entidade que irá gerenciar o site Web;
# render_template = carregar um template de página
from flask import Flask, render_template


# app é o nome do Site Web
# __name__ é uma variável do Python
app = Flask(__name__)

# Criar a 1 primeira pagina do site
# route -> para direcionar para qual pagína dentro do seu Site, treinamentos.com/contatos
# template

# linha de codigo que atribui uma nova função para a função "def home()"
@app.route('/') # apenas / para acesso a "home.html"
def home(): # função -> def home()
    return render_template("home.html") # carrega o template de Home

# apenas /contatos para acesso a Home -> arquivo HTML dentro pasta "templates"
@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html") # carrega um template de Contatos

# apenas /contatos para acesso a Home -> arquivo HTML dentro pasta "templates"
@app.route("/contato.html")
def contato():
    return render_template("contato.html") # carrega um template de Contatos


# Criar páginas de forma dinâmica: criacao de uma pagina para cada usuario
# <nome_usuario> aqui sera o nome do usuario
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
    # 4 Passos para usar variavel


# app.run() = executa o site (o if somente será executado quando esse arquivo for executado individual)
# __name__ = variável de sistema, recebe valor __main__ (nome arquivo local) automático
if __name__ == '__main__':
    app.run(debug=True) # debug para rodar o codigo direto para toda alteração

