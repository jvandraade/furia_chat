import requests
from bs4 import BeautifulSoup

def get_noticias_hltv():
    url = "https://www.hltv.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    noticias = []
    articles = soup.select(".newsline article")

    for article in articles[:5]:
        titulo = article.select_one("a").text.strip()
        link = "https://www.hltv.org" + article.select_one("a")["href"]
        noticias.append({"titulo": titulo, "link": link})

        return noticias