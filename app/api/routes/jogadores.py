from fastapi import APIRouter, Query
from app.api.services.player_info import buscar_info_jogador

router = APIRouter(prefix="/jogadores", tags=["Jogadores"])

@router.get("/buscar")
def buscar_jogador(nome_jogador: str = Query(..., description="Nome do jogador")):
    return buscar_info_jogador(nome_jogador)