from googlelyrics import search


def test_lyrics():
    lyrics = search("oasis wonderwall")

    assert lyrics.artist == "Oasis"
    assert lyrics.title == "Wonderwall"

    assert len(lyrics.lines) > 30
    assert lyrics.lines[0] == "Today is gonna be the day that they're gonna throw it back to you"
    assert lyrics.lines[-1] == "You're gonna be the one that saves me (saves me)"


def test_not_found():
    lyrics = search("___qqqqwwweeee___")

    assert lyrics is None
