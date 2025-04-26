from fastapi import APIRouter, Query
from typing import List
from app.api.services.conteudos_service import listar_conteudos
from app.api.models.conteudo import Conteudo

router = APIRouter(prefix="/conteudos", tags=["Conteudos"])

@router.get("/")
def get_conteudos(jogador: str = Query(None), tipo: str = Query(None)):
    return listar_conteudos(jogador, tipo)