from apscheduler.schedulers.background import BackgroundScheduler
from app.api.websocket.connection import connections
from app.api.services.social_monitor import get_youtube_latest_video

scheduler = BackgroundScheduler()

def send_social_notifications():
    url = get_youtube_latest_video("https://www.youtube.com/@FURIAggVAL")
    if url:
        for ws in connections:
            try:
                ws.send_text(f"🎥 Novo vídeo no canal da FURIA! Assista agora: {url}")
            except:
                connections.remove(ws)

def start_scheduler():
    scheduler.add_job(send_social_notifications, 'interval', minutes = 5)
    scheduler.start()      