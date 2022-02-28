

from schemas.usuario import UsuarioBase
from database.hashing import Hash

from database.db import conn

from fastapi import Depends

from bson import ObjectId

from database.db import get_usuario_collection

def create (request: UsuarioBase, usuarios):
    new_usuario = request.dict(by_alias=True)
    new_usuario["password"] = Hash.bcrypt (new_usuario["password"])
    conn.usuarios.insert_one(new_usuario)
    return new_usuario


def get_all(usuarios):  
    return list(usuarios.find())

def edit_about(id:str,about: str, ids= Depends(get_usuario_collection)):
    newAbout = ids.update_one({"_id": ObjectId(id)}, {"$set":{"about": about}})
    return newAbout

def edit_profpic(id:str,profilePicture: str, ids= Depends(get_usuario_collection)):
    newPicture = ids.update_one({"_id": ObjectId(id)}, {"$set":{"profilePicture": profilePicture}})
    return newPicture

def edit_profession(id:str,profession: str, ids= Depends(get_usuario_collection)):
    newProfession = ids.update_one({"_id": ObjectId(id)}, {"$set":{"profession": profession}})
    return newProfession

def deleteUser(id:str, ids= Depends(get_usuario_collection)):
    deletedAcount = ids.delete_one({"_id": ObjectId(id)})
    return deletedAcount

def get_by_id(id: str, ids = Depends(get_usuario_collection)):
    id = ids.find_one({'_id':ObjectId(id)})
    return id

def get_by_email(email: str, usuarios = Depends(get_usuario_collection)):
    usuario = usuarios.find_one({'email':email})
    return usuario



