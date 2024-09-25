"VerticalHistogram"
def main() :
    "main"
    text = sorted(filter(lambda x : x.isalpha(), input()))
    letter = dict.fromkeys(text,0)
    board = ""

    for i in text :
        letter[i] += 1

    most = max(letter.values())


    for i in range(most,0,-1) :
        print(f"{i:>2}",end="  ")
        for j in letter.values() :
            board += " "*(j < i)+"*"*(j >= i)+" "
        print(board)
        board = ""

    print("    ",end="")
    print(" ".join(letter))
main()
