from database.db import get_vaga_collection
from schemas.vaga import VagaBase

from bson import ObjectId
from jose import jwt, JWTError
from datetime import datetime, timedelta

from fastapi import HTTPException, Depends, status

from repositories import usuario as User

from fastapi.security import OAuth2PasswordBearer

from database.db import get_user_collection

def createVaga (request: VagaBase, vagas):
    new_vaga = request.dict(by_alias=True)
    vagas.insert_one(new_vaga)
    return request

def get_by_id_vaga(id: str, ids = Depends(get_vaga_collection)):
    id = ids.find_one({'_id':ObjectId(id)})
    return id
    
def get_all_vagas(vaga):
    return list(vaga.find())

def get_current_user(token: str = Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user =  User.get_by_email(email, get_usuario_collection())
    if user is None:
        raise credentials_exception
    return user