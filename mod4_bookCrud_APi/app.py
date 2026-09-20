from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_books.db'
db = SQLAlchemy(app)

#define db model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80))
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f'{self.book_name} written by {self.author} and published by {self.publisher}'

@app.route('/')
def hello():
    return 'Hewwo XD'

@app.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)
    return {'books': output}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return f'{book.book_name} has been added'

@app.route('/books', methods=['DELETE'])
def burn_book():
    name = request.json['book_name']
    Book.query.get(name)
    if book is None:
        return 'book not found'
    db.session.delete(book)
    db.session.commit()
    return f'{book.book_name} has been removed'
