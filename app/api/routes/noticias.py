from fastapi import APIRouter

router = APIRouter()

@router.get("/noticias")
async def get_noticias():
    return {"mensagem": "Aqui estão as notícias"}
