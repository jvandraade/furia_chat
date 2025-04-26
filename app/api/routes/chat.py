from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

@router.get("/")
def get_status():
    return {"status": "chat online"}