pop = []
jpop = []

def collect_songs():
    song = "Type a pop song: "
    ask = "Type p or j. Type q to exit.: "

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            j = input(song)
            jpop.append(j)

        else:
            print("Invalid value")

    print("pop songs: ", pop)
    print("jpop songs: ", jpop)

collect_songs()
