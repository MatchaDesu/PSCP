"RemoveTag"
def main() :
    "main"
    word = input()
    word = word.replace(">","@?").replace("<","?@")
    word = word.split("?")
    new_word = []
    printable = []

    for i in word :
        if not "@" in i :
            new_word.append(i)
    new_word = " ".join(new_word).split(" ")

    for i in new_word :
        if i :
            printable.append(i)
    print(printable)
main()
