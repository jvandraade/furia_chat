from fastapi import APIRouter
from app.api.services.eventos_service import listar_eventos

router = APIRouter(prefix="/eventos", tags=["Eventos"])

@router.get("/")
def get_eventos():
    return listar_eventos()