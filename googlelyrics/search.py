from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
)


@dataclass
class Lyrics:
    title: str
    artist: str
    lines: List[str]


def find_containers(soup):
    container = soup.find(attrs={"data-attrid": "kc:/music/recording_cluster:lyrics"})

    if not container:
        return (None, None)

    lyrics_container = container.find(lambda tag: tag.has_attr("data-lyricid"))
    header_container = container.parent.parent.previous_sibling

    return (lyrics_container, header_container)


def extract_blocks(container):
    blocks = list(container.contents[0])[:-1]
    blocks.extend(container.contents[1])
    return blocks


def extract_header_info(container):
    title = container.find(attrs={"data-attrid": "title"}).find("span").text
    artist = container.find(attrs={"data-attrid": "subtitle"}).find("a").text

    return (title, artist)


def search(query):
    if "lyrics" not in query:
        query = f"{query} lyrics"

    rsp = requests.get(
        "https://www.google.com/search",
        params={"q": query},
        headers={"user-agent": USER_AGENT},
    )

    rsp.raise_for_status()

    soup = BeautifulSoup(rsp.text, features="html.parser")

    lyrics_container, header_container = find_containers(soup)

    if not lyrics_container:
        return None

    lines = []

    for block in extract_blocks(lyrics_container):
        if lines:
            lines.append("")

        lines.extend(line.text for line in block.find_all("span"))

    title, artist = extract_header_info(header_container)

    return Lyrics(title, artist, lines)
