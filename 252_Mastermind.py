"Mastermind"
def main() :
    "main"
    ans = input()
    guess = input()
    counted = []
    color = []

    for i in range(4) :
        for j in range(4) :
            if ans[i] == guess[j] and j not in counted :
                if i == j :
                    color.append("B")
                elif guess[i] != ans[i] and guess[j] != ans[j]:
                    color.append("W")
                else :
                    continue
                counted.append(j)
                break

    color.extend(["O"]*(4-len(color)))
    color.sort(key=lambda x : (x in "O",x in "W",x in "B"))
    print("".join(color))

main()
