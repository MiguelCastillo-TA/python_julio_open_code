import os

from flask import flash
from flask_base.config.mysqlconnection import connectToMySQL
from flask_base.models.modelo_base import ModeloBase


class Magazine(ModeloBase):

    modelo = 'magazine'
    campos = ['title','description','user_id']

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        self.user_name = data['user_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = f"SELECT magazine.*, CONCAT(user.name, ' ', user.last_name) as user_name FROM magazine JOIN user ON user.id = user_id;"
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query)
        print(results)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT magazine.*, CONCAT(user.name, ' ', user.last_name) as user_name FROM magazine JOIN user ON user.id = user_id WHERE magazine.id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_all_user_magazines(cls, id):
        query = f"SELECT magazine.*, CONCAT(user.name, ' ', user.last_name) as user_name FROM magazine JOIN user ON user.id = user_id WHERE user.id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print(results)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @staticmethod
    def validar_largo(data, campo, largo):
        is_valid = True
        if len(data[campo]) <= largo:
            flash(f'El largo del {campo} no puede ser menor o igual {largo}', 'error')
            is_valid = False
        return is_valid
    
    @classmethod
    def validar(cls, data):

        is_valid = True

        is_valid = cls.validar_largo(data, 'title', 2)
        is_valid = cls.validar_largo(data, 'description', 10)

        return is_valid
