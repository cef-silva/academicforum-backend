
from database.hashing import Hash
from schemas.empresa import EmpresaBase, EmpresaDisplay
from database.db import get_empresa_collection
from database.db import conn
from fastapi import Depends
from bson import ObjectId


def createEmpresa (request: EmpresaBase, empresas):
    new_empresa = request.dict(by_alias=True)
    new_empresa["password"] = Hash.bcrypt (new_empresa["password"])
    conn.empresas.insert_one(new_empresa)
    return new_empresa

def get_by_email(email: str, empresas = Depends(get_empresa_collection)):
    empresa = empresas.find_one({'email':email})
    return empresa

def get_all(empresas):  
    return list(empresas.find())

