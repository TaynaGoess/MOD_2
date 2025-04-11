from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def setup_database():
    with sqlite3.connect('library.db') as connection:
        connection.execute('CREATE TABLE IF NOT EXISTS books ('
                           'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                           'title TEXT NOT NULL, '
                           'category TEXT NOT NULL, '
                           'author TEXT NOT NULL, '
                           'image_url TEXT NOT NULL)')
        print('Tabela BOOKS criada com sucesso.')

setup_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    category = data.get('category')
    author = data.get('author')
    image_url = data.get('image_url')

    if not all([title, category, author, image_url]):
        return jsonify({'Error': 'Todos os campos são obrigatórios'}), 400

    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books (title, category, author, image_url) VALUES (?, ?, ?, ?)',
                       (title, category, author, image_url))
        connection.commit()

    return jsonify({'Message': 'Livro registrado com sucesso!'}), 201

@app.route('/books', methods=['GET'])
def get_books():
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()

    books_list = [{'id': book[0], 'title': book[1], 'category': book[2],
                   'author': book[3], 'image_url': book[4]} for book in books]

    return jsonify({'books': books_list}), 200

@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (id,))
        connection.commit()

    if cursor.rowcount == 0:
        return jsonify({'Error': 'Livro não encontrado'}), 404

    return jsonify({'Message': 'Livro removido com sucesso!'}), 200

if __name__ == "__main__":
    app.run(debug=True)