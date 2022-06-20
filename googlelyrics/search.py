from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
)


@dataclass
class Lyrics:
    title: str
    artist: str
    lines: List[str]


def find_lyrics(soup):
    container = soup.find(attrs={"data-attrid": "kc:/music/recording_cluster:lyrics"})
    if not container:
        return None

    container = container.find(lambda tag: tag.has_attr("data-lyricid"))
    return container.contents[0].contents[1].contents


def find_attrid(soup, data_attrid):
    container = soup.find(attrs={"data-attrid": data_attrid})
    if not container:
        return None

    return container.contents[0].text


def find_title(soup):
    return find_attrid(soup, "title")


def find_artist(soup):
    return find_attrid(soup, "subtitle")


def search(query):
    if "lyrics" not in query:
        query = f"{query} lyrics"

    rsp = requests.get(
        "https://www.google.com/search",
        params={"q": query},
        headers={"User-Agent": USER_AGENT},
    )

    rsp.raise_for_status()

    soup = BeautifulSoup(rsp.text, features="html.parser")
    lyrics_container = find_lyrics(soup)

    if not lyrics_container:
        return None

    lines = []

    for block in lyrics_container:
        if lines:
            lines.append("")

        lines.extend(line.text.strip() for line in block.find_all("span"))

    artist = find_artist(soup)
    title = find_title(soup)

    if artist:
        artist = artist.split(" ", 2)[2]

    return Lyrics(title, artist, lines)
