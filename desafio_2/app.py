from flask import Flask, request, jsonify
from database import db, Livro

# Inicializa o aplicativo Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return "API de Livros VnW!"

@app.route('/cadastrar', methods=['POST'])
def cadastrar_livro():
    """Rota para cadastrar um novo livro."""
    dados_livro = request.get_json()
    

    if not dados_livro:
        return jsonify({"erro": "Nenhum dado fornecido"}), 400


    campos_obrigatorios = ["titulo", "categoria", "autor", "url_imagem"]
    for campo in campos_obrigatorios:
        if campo not in dados_livro or not dados_livro[campo]:
            return jsonify({"erro": f"Campo '{campo}' é obrigatório."}), 400

    novo_livro = Livro(
        titulo=dados_livro['titulo'],
        categoria=dados_livro['categoria'],
        autor=dados_livro['autor'],
        url_imagem=dados_livro['url_imagem']
    )

    db.session.add(novo_livro)
    db.session.commit()
    
    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201

@app.route('/livros', methods=['GET'])
def listar_livros():
    """Rota para listar todos os livros cadastrados."""
    livros = Livro.query.all()
    resultado = []
    
    for livro in livros:
        resultado.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "categoria": livro.categoria,
            "autor": livro.autor,
            "url_imagem": livro.url_imagem
        })
    
    return jsonify(resultado)

# Executando o aplicativo
if __name__ == '__main__':
    app.run(debug=True)