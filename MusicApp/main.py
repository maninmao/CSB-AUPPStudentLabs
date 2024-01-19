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

    def search_playlist(self, query):
        results = []
        for song in self.songs:
            if query.lower() in song.title.lower() or query.lower() in song.artist.lower():
                results.append(song)
        return results

# Create a music library.
library = MusicLibrary()

# Add songs to the music library.
library.add_song(Song("W/X/Y", "Tani Yuuki", "W/X/Y", "J-Pop", "4:38"))
library.add_song(Song("HAREHAREYA", "UniteUp!", "HAREHAREYA", "J-Pop", "3:28"))
library.add_song(Song("FLY HIGH!!", "BURNOUT SYNDROMES", "HAIKYUU", "J-Pop", "4:04"))
library.add_song(Song("Prologue", "YOASOBI", "Prologue", "J-Pop", "4:35"))
library.add_song(Song("Ghost Rule", "Yorushika", "That's Why I Gave Up on Music", "J-Pop", "4:15"))
library.add_song(Song("MANIAC", "Stray Kids", "Oddinary", "K-Pop", "3:03"))
library.add_song(Song("Hakuna Matata", "Yorushika", "Plagiarism", "J-Pop", "4:01"))
library.add_song(Song("365 Nichi no Love Letter", "AKB48", "Tsugi no Ashiato", "J-Pop", "4:43"))
library.add_song(Song("Koi wa Cristal", "CHiCO with HoneyWorks", "Kokuhaku Yokou Renshuu", "J-Pop", "4:12"))
library.add_song(Song("FAKE", "DISH//", "Junkfood Junction", "J-Pop Rock", "3:46"))
library.add_song(Song("Walk on memories", "EXO", "The War", "K-Pop", "3:52"))
library.add_song(Song("Overdose", "EXO", "Overdose", "K-Pop", "3:38"))
library.add_song(Song("Paper Cuts", "EXO-CBX", "EXO-CBX “MAGICAL CIRCUS” 2019", "K-Pop", "3:45"))
library.add_song(Song("April, and a Flower", "Chen", "April, and a Flower", "K-Pop Ballad", "3:35"))
library.add_song(Song("BOSS", "NCT", "BOSS", "K-Pop", "3:31"))
library.add_song(Song("Campfire", "SEVENTEEN", "Ode to you", "K-Pop R&B", "3:27"))
library.add_song(Song("7PM", "BSS", "7PM", "K-Pop Hip-Hop", "3:15"))
library.add_song(Song("Gurenge", "LiSA", "Gurenge", "J-Pop Anime", "3:54"))
library.add_song(Song("Imagination", "SPYAIR", "Just Do It", "J-Pop Anime Rock", "4:13"))
library.add_song(Song("Drowning", "WOODZ", "OO-LI", "K-Pop", "4:05"))
library.add_song(Song("Renegades", "ONE OK ROCK", "Renegades", "J-Pop", "4:05"))

# Get songs by artist
artist = "Yorushika"
songs_by_artist = library.get_songs_by_artist(artist)
print("-------------------------------------------")
print(f"{artist} songs:")
for song in songs_by_artist:
    print(f"{song.title} by {song.artist}")
print("-------------------------------------------")

# Create a playlist.
playlist = Playlist()

# Add some songs to the playlist.
playlist.add_song(library.get_songs_by_title("FLY HIGH!!")[0])
playlist.add_song(library.get_songs_by_title("Renegades")[0])
playlist.add_song(library.get_songs_by_title("Campfire")[0])
playlist.add_song(library.get_songs_by_title("W/X/Y")[0])
playlist.add_song(library.get_songs_by_title("Prologue")[0])
playlist.add_song(library.get_songs_by_title("MANIAC")[0])
playlist.add_song(library.get_songs_by_title("7PM")[0])
playlist.add_song(library.get_songs_by_title("Overdose")[0])
playlist.add_song(library.get_songs_by_title("BOSS")[0])
playlist.add_song(library.get_songs_by_title("W/X/Y")[0])
playlist.add_song(library.get_songs_by_title("Paper Cuts")[0])
playlist.add_song(library.get_songs_by_title("Walk on memories")[0])
playlist.add_song(library.get_songs_by_title("HAREHAREYA")[0])
playlist.add_song(library.get_songs_by_title("Hakuna Matata")[0])
playlist.remove_song(library.get_songs_by_title("Paper Cuts")[0])

# Display the playlist.​​​​​​​​​​​​
print("         ~~~~​​​​​​​​ ​​​​My Playlist  ~~~~         ")
print("-------------------------------------------")
playlist.display_playlist()
print("-------------------------------------------")

# Search for a song or artist in the playlist.
# Get user input
query = input("    Search a song or artist name: ")


# Search for a song or artist in the playlist.
results = playlist.search_playlist(query)

# Display search results
if results:
    print()
    print("Search results:"'\n')
    for result in results:
        print(f"         {result.title} by {result.artist}""\n")
else:
    print("\n")
    print("          No results found.""\n")


# Main Requirement:
# Create song example =
# Create a music library =
# Add songs to the music library =
# Get songs by artist = 
# Create playlists =
# Add songs to playlists = 
# Display playlists
# Searching for songs by artist