"Volleyball"
def main() :
    "main"
    match = str(input())
    counta, countb = 0, 0
    a_win, b_win = 0,0
    set_match = 1
    recap = ""

    for i in match :
        if i in "A" :
            counta += 1
        elif i in "B" :
            countb += 1
        if set_match != 5 and (counta >= 25 or countb >= 25) and abs(counta-countb) >=2 :
            recap += f"Set {set_match}: A ({counta}) | B ({countb})\n"
            set_match += 1

            if counta > countb :
                a_win += 1
            else :
                b_win += 1

            counta,countb = 0,0
        elif set_match == 5 and (counta >= 15 or countb >= 15) and abs(counta-countb) >=2 :
            recap += f"Set {set_match}: A ({counta}) | B ({countb})\n"

            if counta > countb :
                a_win += 1
            else :
                b_win += 1

            counta,countb = 0,0

    if a_win < 3 and b_win < 3 :
        recap += f"Set {set_match}: A ({counta}) | B ({countb})\n"
        recap += "The game has not finished yet."
    else :
        if a_win > b_win :
            recap += f"A won {a_win}:{b_win} set"
        else :
            recap += f"B won {b_win}:{a_win} set"
    print(recap)
main()
