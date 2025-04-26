from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import chat, noticias
from app.api.websocket.connection import router as websocket_router

app = FastAPI(title = "Furia Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(noticias.router)
app.include_router(websocket_router)
