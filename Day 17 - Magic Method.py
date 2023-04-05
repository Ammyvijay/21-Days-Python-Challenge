"""
Note : Magic methods in Python are special methods that allow classes to define their own behavior for built-in operations. They are denoted by double underscores before and after their names (e.g., __len__, __str__).

The benefits of using magic methods include making code more intuitive and easier to read, reducing code redundancy, and allowing for customization of built-in operations to fit specific use cases.
"""

class Playlist:

    def __init__(self,songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)
    
    def __getitem__(self,index):
        return self.songs[index]
    
    def __setitem__(self,index:int,song:str):
        self.songs[index]=song

    def __str__(self):
        return f"Playlist with {len(self)} songs."
    
# Create a new playlist with few songs
my_playlist = Playlist(['A','B','C','D'])

print(len(my_playlist))
print(my_playlist[1])
print(my_playlist)
my_playlist[0]="One"
print(my_playlist[0])