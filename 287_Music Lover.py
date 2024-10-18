"Music Lover"
def main() :
    "main"
    album = {}
    for i in range(int(input())) :
        singer, song = input().split("-")
        if singer not in album :
            album[singer] = []
        album[singer].append(song.strip())

    for i,j in album.items() :
        print(i)
        for song in j :
            print(song)

main()
