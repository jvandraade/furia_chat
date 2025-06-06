from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import chat, noticias, jogadores, eventos, conteudos, loja
from app.api.websocket.connection import router as websocket_router
from app.api.tasks.notifier import start_scheduler

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
app.include_router(jogadores.router)
app.include_router(eventos.router)
app.include_router(conteudos.router)
app.include_router(loja.router)

@app.get("/")
def read_root():
    return {"mensagem": "Bem vindo à API da Furia Chatbot! Use as rotas para acessas os conteúdos."}

# Notificações de novos conteúdos em rede social
start_scheduler()

load_dotenv()