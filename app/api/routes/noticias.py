from fastapi import APIRouter
from app.api.services.noticias import get_noticias_hltv

router = APIRouter(prefix="/noticias", tags=["Notícias"])

@router.get("/")
def listar_noticias():
    return {"notícias": get_noticias_hltv()}
