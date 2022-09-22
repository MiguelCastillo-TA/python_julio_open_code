import os

from flask import flash
from flask_base.config.mysqlconnection import connectToMySQL
from flask_base.models.modelo_base import ModeloBase
from flask_base.utils.regex import REGEX_CORREO_VALIDO


class Usuario(ModeloBase):

    modelo = 'usuarios'
    campos = ['nombre','apellido','email','password']

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def buscar(cls, dato):
        query = "select * from usuarios where email = %(dato)s"
        data = { 'dato' : dato }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = """UPDATE usuarios 
                        SET nombre = %(nombre)s,
                        SET apellido = %(apellido)s,
                        SET email = %(email)s,
                        SET password = %(password)s,
                        SET usuario = %(usuario)s,
                        updated_at=NOW() 
                    WHERE id = %(id)s"""
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

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

        is_valid = cls.validar_largo(data, 'nombre', 3)

        if not REGEX_CORREO_VALIDO.match(data['email']):
            flash('El correo no es válido', 'error')
            is_valid = False

        if data['password'] != data['cpassword']:
            flash('las contraseñas no son iguales', 'error')
            is_valid = False

        if cls.validar_existe('email', data['email']):
            flash('el email ya esta ingresado', 'error')
            is_valid = False

        return is_valid
