import os

from flask_base.config.mysqlconnection import connectToMySQL

class ModeloBase():

    # modelo = '' indicar modelo
    # campos = [] aca indicar todos los campos del hijo

    @classmethod
    def validar_existe(cls, campo, valor):
        query = f"SELECT count(*) as contador FROM {cls.modelo} WHERE {campo} = %({campo})s;"
        data = { campo : valor }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        return results[0]['contador'] > 0

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.modelo};"
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data


    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {cls.modelo} WHERE id = %(id)s"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        return results


    @classmethod
    def delete(cls,id):
        query = f"DELETE FROM {cls.modelo} WHERE id = %(id)s"
        data = {
            'id': id
        }
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado      
        
    @classmethod
    def save(cls, data):

        campos_header = ''
        campos_datos = ''
        for campo in cls.campos:
            campos_header += campo + ','
            campos_datos += f'%({campo})s,'

        query = f"""
                INSERT INTO {cls.modelo} ({campos_header}created_at, updated_at)
                VALUES ({campos_datos} NOW(), NOW());
                """
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado