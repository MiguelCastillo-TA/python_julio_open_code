from app.config.mysqlconnection import connectToMySQL
from app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def add_dojo(cls, data):
        query =  "INSERT INTO dojos (name) VALUES (%(name)s)"
        results = connectToMySQL('dojos_y_ninjas').query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_y_ninjas').query_db(query)
        print(results)
        if len(results) == 0:
            return None
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id=%(dojo_id)s;"
        results = connectToMySQL('dojos_y_ninjas').query_db(query, data)
        print(results)
        if len(results) == 0:
            return None
        dojo_data = {
            'id': results[0]['id'],
            'name':  results[0]['name'],
            'created_at': results[0]['created_at'],
            'updated_at': results[0]['updated_at'] 
        }
        dojo = Dojo(dojo_data)
        all_ninjas = []
        for data in results:
            print('*'*20)
            print(data)
            ninja_data = {
                'id': data['ninjas.id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'age': data['age'],
                'created_at': data['ninjas.created_at'],
                'updated_at': data['ninjas.updated_at']
            }
            new_ninja = Ninja(ninja_data)
            print(new_ninja)
            all_ninjas.append(new_ninja)
        dojo.ninjas = all_ninjas
        return dojo

    
    