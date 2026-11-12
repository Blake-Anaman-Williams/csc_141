def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album

print(make_album("Drake", "Views"))
print(make_album("Travis Scott", "Utopia"))
print(make_album("The Weeknd", "After Hours"))
print(make_album("Drake", "Scorpion", 25))