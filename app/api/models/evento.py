from pydantic import BaseModel
from datetime import datetime

class Evento(BaseModel):
    nome: str
    data: datetime
    local: str
    link_oficial: str