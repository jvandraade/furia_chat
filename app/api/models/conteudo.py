from pydantic import BaseModel

class Conteudo(BaseModel):
    titulo: str
    descricao: str
    link: str
    jogador: str
    tipo: str