from fastapi import APIRouter
from app.api.services.loja_service import obter_link_loja

router = APIRouter(prefix="/loja", tags=["Loja"])

@router.get("/")
def get_link_loja():
    return {"link": obter_link_loja()}