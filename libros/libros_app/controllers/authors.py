from libros_app import app
from libros_app.models.author import Author
from flask import render_template, request, redirect, flash

@app.route('/authors')
def authors():
    all_authors = Author.get_all()
    return render_template('authors/authors.html', authors=all_authors)

@app.route('/authors/process', methods=['POST'])
def add_author():
    data = {
        'name': request.form['name']
    }
    new_author = Author.add_author(data)
    if new_author == False:
        print('creating error message')
        flash("Error Creating Author", "error")
    return redirect('/authors')

@app.route('/authors/<int:id>')
def author_details(id):
    data = {
        "id": id
    }
    author = Author.get_author_favorite_books(data)
    print(author)
    return render_template('authors/authorDetails.html', author=author)