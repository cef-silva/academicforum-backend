from fastapi import APIRouter, Depends

from schemas.vaga import VagaDisplay, VagaBase
from database.db import conn
from bson import ObjectId

from typing import List

from schemas.usuario import UserAuth


from database.db import get_vaga_collection
from repositories import vaga


router = APIRouter (
    prefix='/vagas',
    tags=['vagas']
)


@router.post('/', response_model=VagaDisplay)
def createVaga(request: VagaBase, vagas = Depends(get_vaga_collection)):
    return vaga.createVaga(request, vagas)

@router.put("/id/edit-titulo")
def edit_titulo( id: str, title:str, vagas = Depends(get_vaga_collection)):
    vaga.edit_titulo( id, title, vagas)
    return {"mensagem": "Nome da vaga foi atualizado"}

@router.put("/id/edit-description")
def edit_descricao( id: str, descricao:str, vagas = Depends(get_vaga_collection)):
    vaga.edit_descricao( id, descricao, vagas)
    return {"mensagem": "Descrição foi atualizada"}


@router.put("/id/edit-details")
def edit_detalhe( id: str, detalhes:str, vagas = Depends(get_vaga_collection)):
    vaga.edit_detalhe( id, detalhes, vagas)
    return {"mensagem": "Detalhes foram atualizadas"}

@router.put("/id/edit-type")
def edit_type( id: str, tipoVaga:str, vagas = Depends(get_vaga_collection)):
    vaga.edit_type( id, tipoVaga, vagas)
    return {"mensagem": "O tipo da vaga foi atualizado"}

@router.put("/id/edit-image")
def edit_image( id: str, image:str, vagas = Depends(get_vaga_collection)):
    vaga.edit_image( id, image, vagas)
    return {"mensagem": "A imagem foi atualizada"}

@router.get("/", response_model=List[VagaDisplay])
def vagaShow(vagas = Depends(get_vaga_collection)):
    return vaga.get_all_vagas(vagas)

@router.delete("/")
def deleteVaga(id:str, vagas = Depends(get_vaga_collection)):
    vaga.deleteVaga(id, vagas)
    return {"mensagem": "A vaga foi deletada"}

@router.get("/id", response_model= VagaDisplay)
def get_by_id(id:str, vagas=Depends(get_vaga_collection)):
    return vaga.get_by_id(id, vagas)
