from flask_sqlalchemy import SQLAlchemy

# Inicializa o objeto SQLAlchemy
db = SQLAlchemy()

class Livro(db.Model):
    __tablename__ = 'LIVROS'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    url_imagem = db.Column(db.String(200), nullable=False)