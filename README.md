# 🐍 Chatbot FURIA CS — Projeto de Interação com Fãs

Este projeto é um chatbot web desenvolvido para os fãs da equipe de Counter-Strike da organização de eSports **FURIA**. Ele oferece interações em tempo real, push de novidades, integração com redes sociais e muito mais.

---

## ⚙️ Tecnologias Utilizadas

### Backend (Python)
- [FastAPI](https://fastapi.tiangolo.com/) — API Web moderna e performática
- [Twitch API](https://dev.twitch.tv/docs/api/) — Verificação de lives ativas
- [YouTube Data API](https://developers.google.com/youtube/v3) — Checagem de novos vídeos
- [APScheduler](https://apscheduler.readthedocs.io/) — Tarefas programadas (cronjobs)
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI para FastAPI
- [Railway](https://railway.com) — Deploy do backend gratuito

### Frontend
- [React + Vite](https://vitejs.dev/) — Framework leve e moderno
- [TailwindCSS](https://tailwindcss.com/) — Estilização rápida e responsiva
- [Vercel](https://vercel.com/) — Deploy do frontend gratuito

---

## 🚀 Funcionalidades

- ✅ **Chat Web para fãs da FURIA (line de CS2)**
- ✅ **Push Notifications de novos vídeos e lives**
- ✅ **Curiosidades e informações dos jogadores**
- ✅ **Link para loja oficial da FURIA**
- ✅ **Divulgação de calendário de campeonatos**
- ✅ **Rotina e conteúdos exclusivos**
- ✅ **Notificações automáticas agendadas via APScheduler**
- ✅ **Deploy gratuito (Railway + Vercel)**

---

## 🧑‍💻 Como Executar Localmente

### Clonando o projeto

git clone https://github.com/seu-usuario/furia_chat.git
cd furia_chat

cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

### Crie um arquivo .env com:
env

YOUTUBE_API_KEY=xxxx
TWITCH_CLIENT_ID=xxxx
TWITCH_SECRET=xxxx


### 🌐 Frontend (React + Vite)

cd furia_chat_frontend
npm install
npm run dev
No arquivo .env do frontend:

env

VITE_API_URL=http://localhost:8000
VITE_FIREBASE_VAPID_KEY=xxxx 

### 🌍 Deploy
Backend
Realizado via Render.com

Start command: uvicorn app.main:app --host=0.0.0.0 --port=10000

### Frontend
Realizado via Vercel
