# googlelyrics

Utility to show lyrics right in your console. Grabs the lyrics from Google search results.

## Usage

Clone repository and use Pip to install Python module:

```
$ pip install --user ./googlelyrics
```

Run installed launcher with `artist title` query:

```
$ googlelyrics Oasis Wonderwall

Oasis - Wonderwall

Today is gonna be the day
That they're gonna throw it back to you
...
```

Query provided will be passed to Google with `lyrics` added. Note that Google may return
lyrics for a different song.
