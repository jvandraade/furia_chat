from fastapi import APIRouter, WebSocket
from typing import List

router = APIRouter()

connections: List[WebSocket] = []

@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            msg = await websocket.receive_text()
            for conn in connections:
                await conn.send_text(f"Furia bot: {msg}")
    except Exception:
        connections.remove(websocket)