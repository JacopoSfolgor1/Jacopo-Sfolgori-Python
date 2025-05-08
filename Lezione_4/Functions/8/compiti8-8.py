
'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() 
with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.'''

def make_album(artist_name: str, music_title: str, number_songs: int = None):
    music_album: dict = {"artist name": artist_name, "music title" : music_title, "number songs" : number_songs}
    if number_songs == None:
        music_album = {"artist name": artist_name, "music title" : music_title}
    return music_album
    
while True: 
    album_artist = input("insert album artist")
    if album_artist == "Quit": 
        break 
    album_title = input("insert album title")
    print(make_album(album_artist,album_title))