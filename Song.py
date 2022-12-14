class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        playlist = {self}
        song = self.next

        while song:            
            if song in playlist:
                return True

            playlist.add(song)
            song = song.next

        return False
            
first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("test")
    
first.next_song(second)
second.next_song(third)
third.next_song(first)

print(first.is_in_repeating_playlist())