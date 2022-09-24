from crypt import methods

from flask import flash, redirect, render_template, request
from libros_app import app
from libros_app.models.author import Author
from libros_app.models.book import Book


@app.route('/books')
def books():
    all_books = Book.get_all()
    return render_template('books/books.html', books=all_books)

@app.route('/books/process', methods=['POST'])
def add_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    new_book = Book.add_book(data)
    if new_book == False:
        print('creating error message')
        flash("Error Creating book", "error")
    return redirect('/books')

@app.route('/books/<int:id>')
def books_details(id):
    data = {
        "id": id
    }
    book = Book.get_books_favorite_authors(data)
    print(book)
    if book != False:
        print(book)
        authors = []
        for author in book.authors:
            authors.append(Author(author))

        book.authors = authors
    all_authors = Author.get_all()
    return render_template('books/booksDetails.html', book=book, all_authors=all_authors)

@app.route('/add_new_author_favorites', methods=['POST'])
def add_author_to_book():
    data = {
        "authors_id": request.form['author_id'],
        "books_id": request.form['book_id']
    }
    Book.add_favorite_author(data)
    return redirect('/books')
