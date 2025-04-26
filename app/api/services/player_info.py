import wikipedia

wikipedia.set_lang("pt")

def buscar_info_jogador(nome_jogador: str):
    try:
        resumo = wikipedia.summary(nome_jogador, sentences=3)
        pagina = wikipedia.page(nome_jogador)
        return {"resumo": resumo, "link": pagina.url}
    except wikipedia.exceptions.PageError:
        return {"erro": "Não encontramos informações sobre este jogador."}
    except wikipedia.exceptions.DisambiguationError:
        return {"erro": "Mais de um jogador com esse nome. Por favor, especifique o jogador."}