from libros_app.config.mysqlconnection import connectToMySQL


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('libros').query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books (title,num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        results = connectToMySQL('libros').query_db(query, data)
        print(results)
        return results

    @classmethod
    def add_favorite_author(cls, data):
        query = "INSERT INTO favorites (authors_id, books_id) VALUES (%(authors_id)s, %(books_id)s);"
        results = connectToMySQL('libros').query_db(query, data)
        print(results)
        return results


    @classmethod
    def get_books_favorite_authors(cls, data):
        query = "SELECT * FROM libros.books JOIN libros.favorites ON favorites.books_id = books.id JOIN libros.authors ON favorites.authors_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('libros').query_db(query, data)
        print(results)
        if len(results) == 0:
            return False

        book = cls(results[0])
        print(book)
        favorite_authors = []
        for data in results:
            author_data = {
                'id': data['authors.id'],
                'name': data['name'],
                'created_at': data['authors.created_at'],
                'updated_at': data['authors.updated_at']
            }
            favorite_authors.append(author_data)

        book.authors = favorite_authors
        return book

