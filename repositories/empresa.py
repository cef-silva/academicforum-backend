
from database.hashing import Hash
from schemas.empresa import EmpresaBase, EmpresaDisplay
from database.db import get_empresa_collection, get_usuario_collection
from database.db import conn
from fastapi import Depends
from bson import ObjectId



def edit_metier(id:str,metier: str, ids= Depends(get_usuario_collection)):
    newMetier = ids.update_one({"_id": ObjectId(id)}, {"$set":{"metier": metier}})
    return newMetier

def edit_about(id:str,about: str, ids= Depends(get_usuario_collection)):
    newAbout = ids.update_one({"_id": ObjectId(id)}, {"$set":{"about": about}})
    return newAbout

def edit_profpic(id:str,profilePicture: str, ids= Depends(get_usuario_collection)):
    newPicture = ids.update_one({"_id": ObjectId(id)}, {"$set":{"profilePicture": profilePicture}})
    return newPicture

def deleteUser(id:str, ids= Depends(get_usuario_collection)):
    deletedEmpresa = ids.delete_one({"_id": ObjectId(id)})
    return deletedEmpresa

def get_by_email(email: str, empresas = Depends(get_usuario_collection)):
    empresa = empresas.find_one({'email':email})
    return empresa

def get_all(usuarios):  
    return list(usuarios.find())

