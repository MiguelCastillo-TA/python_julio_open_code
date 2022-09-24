from libros_app.config.mysqlconnection import connectToMySQL
from libros_app.models.book import Book


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('libros').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_author_by_id(cls,data):
        query = "SELECT * FROM authors WHERE id=%(id)s;"
        results = connectToMySQL('libros').query_db(query, data)
        # if len(results) > 0:
        #     return cls(results[0])
        # else:
        #     return None
        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def get_author_favorite_books(cls, data):
        query = "SELECT * FROM authors JOIN favorites ON favorites.authors_id = authors.id JOIN books ON favorites.books_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('libros').query_db(query, data)
        print(results)
        author_data = {
                'id': results[0]['id'],
                'name': results[0]['name'],
                'created_at': results[0]['created_at'],
                'updated_at': results[0]['updated_at']
        }
        author = cls(author_data)

        favorite_books = []
        for data in results:
            book_data = {
                'id': data['books.id'],
                'title': data['title'],
                'num_of_pages': data['num_of_pages'],
                'created_at': data['books.created_at'],
                'updated_at': data['books.updated_at']
            }
            book = Book(book_data)
            favorite_books.append(book)
        author.favorites = favorite_books
        return author


    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL('libros').query_db(query, data)
        print(results)
        return results
