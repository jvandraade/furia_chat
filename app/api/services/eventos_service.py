from typing import List
from app.api.models.evento import Evento
from datetime import datetime

eventos = [
    Evento (
        nome="IEM Dallas 2025",
        data=datetime(2025, 5, 27, 15, 0),
        local="Dallas, Texas - EUA",
        link_oficial="https://iem.gg/dallas"
    ),
    Evento (
        nome="BLAST Premier Spring Final 2025",
        data=datetime(2025, 6, 12, 18, 0),
        local="Lisboa, Portugal",
        link_oficial="https://blastpremier.com"
    ),
    Evento (
        nome = "IEM Rio 2025",
        data = datetime(2025, 6, 24, 15, 0),
        local = "Rio de Janeiro, Brasil",
        link_oficial = "https://iem.gg/rio"
    ),
]

def listar_eventos() -> List[Evento]:
    return eventos