from database.db import get_vaga_collection
from schemas.vaga import VagaBase
from bson import ObjectId

from fastapi import HTTPException, Depends, status

def createVaga (request: VagaBase, vagas):
    new_vaga = request.dict(by_alias=True)
    vagas.insert_one(new_vaga)
    return request

def get_by_id_vaga(id: str, ids = Depends(get_vaga_collection)):
    id = ids.find_one({'_id':ObjectId(id)})
    return id
    
def edit_titulo(id:str,titulo: str, ids= Depends(get_vaga_collection)):
    newTitle = ids.update_one({"_id": ObjectId(id)}, {"$set":{"titulo": titulo}})
    return newTitle

def edit_descricao(id:str,descricao: str, ids= Depends(get_vaga_collection)):
    newDescription = ids.update_one({"_id": ObjectId(id)}, {"$set":{"descricao": descricao}})
    return newDescription

def edit_detalhe(id:str,detalhes: str, ids= Depends(get_vaga_collection)):
    newDatail = ids.update_one({"_id": ObjectId(id)}, {"$set":{"destalhes": detalhes}})
    return newDetail

def edit_type(id:str,tipoVaga: str, ids= Depends(get_vaga_collection)):
    newType = ids.update_one({"_id": ObjectId(id)}, {"$set":{"tipoVaga": tipoVaga}})
    return newType

def edit_image(id:str,image: str, ids= Depends(get_vaga_collection)):
    newType = ids.update_one({"_id": ObjectId(id)}, {"$set":{"image": image}})
    return newType

def deleteVaga(id:str, ids= Depends(get_vaga_collection)):
    deletedVaga = ids.delete_one({"_id": ObjectId(id)})
    return deletedVaga

def get_by_id(id: str, ids = Depends(get_vaga_collection)):
    id = ids.find_one({'_id':ObjectId(id)})
    return id

def get_all_vagas(vaga):
    return list(vaga.find())
