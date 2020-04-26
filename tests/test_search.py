from googlelyrics import search


def test_lyrics():
    lyrics = search("oasis hello")

    assert lyrics.artist == "Oasis"
    assert lyrics.title == "Hello"

    assert len(lyrics.lines) == 38
    assert lyrics.lines[0] == "I don't feel as if I know you"
    assert lyrics.lines[-1] == "Hello, hello, hello"


def test_not_found():
    lyrics = search("___qqqqwwweeee___")

    assert lyrics is None
