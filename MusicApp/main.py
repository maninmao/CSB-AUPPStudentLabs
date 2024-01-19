class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length


class MusicLibrary:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_songs_by_artist(self, artist):
        return [song for song in self.songs if song.artist == artist]

    def get_songs_by_album(self, album):
        return [song for song in self.songs if song.album == album]

    def get_songs_by_genre(self, genre):
        return [song for song in self.songs if song.genre == genre]

    def get_songs_by_title(self, title):
        return [song for song in self.songs if song.title == title]

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def reorder_songs(self, new_order):
        self.songs = [song for song in self.songs if song in new_order]

    def display_playlist(self):
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song.title} by {song.artist}")

# Create a music library.
library = MusicLibrary()

# Add some songs to the music library.
library.add_song(Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", "Rock", 360))
library.add_song(Song("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV", "Rock", 480))
library.add_song(Song("Thriller", "Michael Jackson", "Thriller", "Pop", 360))
library.add_song(Song("Imagine", "John Lennon", "Imagine", "Rock", 240))

# Create a playlist.
playlist = Playlist()

# Add some songs to the playlist.
playlist.add_song(library.get_songs_by_title("Imagine")[0])
playlist.add_song(library.get_songs_by_title("Thriller")[0])
playlist.add_song(library.get_songs_by_title("Bohemian Rhapsody")[0])

# Display the playlist.
# playlist.display_playlist()

# Remove a song from the playlist.
playlist.remove_song(library.get_songs_by_title("Thriller")[0])

# Display the playlist.
# playlist.display_playlist()

# Reorder the songs in the playlist.
playlist.reorder_songs([library.get_songs_by_title("Bohemian Rhapsody")[0],
                         library.get_songs_by_title("Imagine")[0]])

# Display the playlist.
playlist.display_playlist()

# Display the songs by Artist 1.
# artist_songs = playlist.get_songs_by_artist("Artist 1")
# print("\nSongs by Artist 1:")
# for song in artist_songs:
#     print(f"{song.title} - {song.album}")