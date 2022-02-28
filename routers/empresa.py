from fastapi import APIRouter, Depends, HTTPException

from schemas.empresa import EmpresaDisplay, EmpresaBase


from database.db import get_empresa_collection, get_usuario_collection

from repositories import empresa, usuario

from typing import List



router = APIRouter (
    prefix='/empresa',
    tags=['empresa']
)


@router.post('/', response_model=EmpresaDisplay )
def createEmpresa(request: EmpresaBase, empresas = Depends(get_usuario_collection)):
    empresaFound = empresa.get_by_email(request.email,empresas)

    if (empresaFound):
        raise HTTPException(status_code=400,
                            detail='Empresa Existente')
    else:
        return usuario.create(request, empresas)


@router.get("/", response_model=List[EmpresaDisplay])
def empresas(empresas = Depends(get_usuario_collection)):
    return empresa.get_all(empresas)

@router.put("/id/edit-about")
def edit_about( id: str, about:str, empresas = Depends(get_usuario_collection)):
    empresa.edit_about( id, about, empresas)
    return {"mensagem": "About foi atualizado"}

@router.put("/id/edit-profpic")
def edit_profpic( id: str, profilePicture:str, empresas = Depends(get_usuario_collection)):
    empresa.edit_profpic( id, profilePicture, empresas)
    return {"mensagem": "Foto de Perfil foi atualizada"}

@router.put("/id/edit-metier")
def edit_profpic( id: str, metier:str, empresas = Depends(get_usuario_collection)):
    empresa.edit_metier( id, metier, empresas)
    return {"mensagem": "Metier foi atualizado"}

@router.delete("/id/delete-empresa")
def deleteUser(id: str, empresas = Depends(get_usuario_collection)):
    empresa.deleteUser(id, empresas)
    return{"mensagem":"Perfil da Empresa deletado"}





