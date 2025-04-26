from typing import List
from app.api.models.conteudo import Conteudo

conteudos = [
    Conteudo(
        titulo="Rotina de Treino do arT",
        descricao="Descubra como o IGL da FURIA organiza seus treinos diários para manter o alto nível.",
        link="https://youtu.be/rotinart",
        jogador="arT",
        tipo="rotina"
    ),
    Conteudo(
        titulo="Dicas de Mira com KSCERATO",
        descricao="O monstro da FURIA ensina como melhorar sua precisão e reação.",
        link="https://youtu.be/dicasksc",
        jogador="KSCERATO",
        tipo="dica"
    ),
    Conteudo(
        titulo="Como o yuurih se prepara para campeonatos",
        descricao="Veja o ritual completo de preparação psicológica e física do yuurih.",
        link="https://youtu.be/rotinayuurih",
        jogador="yuurih",
        tipo="rotina"
    )
]

def listar_conteudos(jogador: str = None, tipo: str = None) -> List[Conteudo]:
    resultado = conteudos

    if jogador:
        resultado = [c for c in resultado if c.jogador.lower() == jogador.lower()]
    if tipo:
        resultado = [c for c in resultado if c.tipo.lower() == tipo.lower()]
    return resultado