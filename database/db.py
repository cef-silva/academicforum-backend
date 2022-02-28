from pymongo import MongoClient
import os


client = MongoClient(os.getenv('MONGODB_URI'))
database_name =  os.getenv('MONGODB_NAME')

conn = client[database_name]

def get_usuario_collection ():
    return conn.usuarios 

def get_empresa_collection():
    return conn.empresas

def get_vaga_collection():
    return conn.vagas