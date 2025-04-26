import requests
from bs4 import BeautifulSoup
import feedparser

def get_youtube_latest_video(channel_url: str):
    rss_url = f"{channel_url}/videos?view=0&sort=dd&flow=grid"
    html = requests.get(rss_url).text
    soup = BeautifulSoup(html, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")
    if href and "/watch?v=" in href:
        return "https://www.youtube.com" + href

    return None

def check_instagram_profile(profile_url: str):
    html = requests.get(profile_url).text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title").text
    return {"desc": title}

def get_twitter_last_post(username: str):
    url = f"https://x.com/{username}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    tweet = soup.find("div", {"class": "tweet-content"})
    return tweet.text.strip() if tweet else None