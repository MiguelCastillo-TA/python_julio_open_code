from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        # SELECT * FROM users;
        query = "SELECT * FROM users;"
        results = connectToMySQL('usuarios_cr').query_db(query)
        all_users = []
        print(f"RESULTS: ", len(results))

        if len(results) == 0:
            return None

        for data in results:
            all_users.append(cls(data))

        return all_users
    @classmethod
    def insert_user(cls, data):
        query = f"INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL('usuarios_cr').query_db(query, data)
        return results
    # INSERT INTO `usuarios_cr`.`users` (`first_name`, `last_name`, `email`) VALUES ('NInja', 'ninja', 'ninja@email.com');

