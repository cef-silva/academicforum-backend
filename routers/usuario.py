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
def edit_about( id: str, about:str, usuarios = Depends(get_usuario_collection)):
    usuario.edit_about( id, about, usuarios)
    return {"mensagem": "About foi atualizado"}

@router.put("/id/edit-profpic")
def edit_profpic( id: str, profilePicture:str, usuarios = Depends(get_usuario_collection)):
    usuario.edit_profpic( id, profilePicture, usuarios)
    return {"mensagem": "Foto de Perfil foi atualizada"}

@router.put("/id/edit-profession")
def edit_profession( id: str, profession:str, usuarios = Depends(get_usuario_collection)):
    usuario.edit_profession( id, profession, usuarios)
    return {"mensagem": "Profissão foi atualizada"}

@router.delete("/id/delete-acount")
def deleteUser(id: str, usuarios = Depends(get_usuario_collection)):
    usuario.deleteUser(id, usuarios)
    return{"mensagem":"Perfil deletado"}

@router.get("/id", response_model=UsuarioDisplay)
def getbyid(id:str, usuarios=Depends(get_usuario_collection)):
   userFound = usuario.get_by_id(id,usuarios)
   return userFound


