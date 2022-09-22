import os

from flask import flash
from flask_base.config.mysqlconnection import connectToMySQL
from flask_base.models.modelo_base import ModeloBase


class Message(ModeloBase):

    modelo = 'messages'
    campos = ['message','usuario_sent_id','usuario_received_id']

    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.usuario_sent_id = data['usuario_sent_id']
        self.usuario_sent_nombre = data['nombre']
        self.usuario_received_id = data['usuario_received_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_user_message_sent_count(cls, data):
        query = "SELECT count(*) as msg_count FROM messages WHERE usuario_sent_id = %(id)s;"
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print(results)
        return results[0]['msg_count']
        # all_data = []
        # for data in results:
        #     all_data.append(cls(data))
        # return all_data

    @classmethod
    def get_all_user_messages(cls, data):
        query = "SELECT * FROM muro_privado.messages JOIN muro_privado.usuarios ON muro_privado.usuarios.id = messages.usuario_sent_id WHERE usuario_received_id = %(id)s;"
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        if len(results) == 0:
            return False
        all_data = []
        # print(results)
        for data in results:
            all_data.append(cls(data))
        return all_data

    
