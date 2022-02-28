from fastapi import APIRouter, Depends, HTTPException

from schemas.usuario import UsuarioDisplay, UsuarioBase


from database.db import get_usuario_collection
from repositories import usuario

from typing import List



router = APIRouter (
    prefix='/usuario',
    tags=['usuario']
)


@router.post('/', response_model=UsuarioDisplay )
def create(request: UsuarioBase, usuarios = Depends(get_usuario_collection)):
    userFound = usuario.get_by_email(request.email,usuarios)

    if (userFound):
        raise HTTPException(status_code=400,
                            detail='Usuario Existente')
    else:
        return usuario.create(request, usuarios)


@router.get("/", response_model=List[UsuarioDisplay])
def usuarioShow(usuarios = Depends(get_usuario_collection)):
    return usuario.get_all(usuarios)

@router.put("/id/edit-about")
def edit_about( id: str, about:str, users = Depends(get_usuario_collection)):
    user.edit_about( id, about, users)
    return {"mensagem": "About foi atualizado"}

@router.put("/id/edit-profpic")
def edit_profpic( id: str, profilePicture:str, users = Depends(get_usuario_collection)):
    user.edit_profpic( id, profilePicture, users)
    return {"mensagem": "Foto de Perfil foi atualizada"}

@router.get("/id", response_model=UsuarioDisplay)
def getbyid(id:str, usuarios=Depends(get_usuario_collection)):
   userFound = user.get_by_id(id,usuarios)
   return userFound


