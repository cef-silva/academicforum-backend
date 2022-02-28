from fastapi import APIRouter, Depends

from schemas.vaga import VagaDisplay, VagaBase
from database.db import conn

from typing import List

from schemas.usuario import UserAuth

from database.db import get_vaga_collection
from repositories import vaga


router = APIRouter (
    prefix='/vagas',
    tags=['vagas']
)


@router.post('/', response_model=VagaDisplay)
def createVaga(request: VagaBase, vagas = Depends(get_vaga_collection), current_user: UserAuth = Depends(vaga.get_current_user)):
    return vaga.createVaga(request, vagas)

@router.get("/", response_model=List[VagaDisplay])
def vagaShow(vagas = Depends(get_vaga_collection)):
    return vaga.get_all_vagas(vagas)

