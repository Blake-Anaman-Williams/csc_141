def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }
    return album

while True:
    artist = input("Enter an artist (or quit): ")

    if artist == "quit":
        break

    title = input("Enter an album title (or quit): ")

    if title == "quit":
        break

    album = make_album(artist, title)
    print(album)