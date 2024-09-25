"Safe"
def main() :
    "main"
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code1 = input()
    code2 = input()
    i = 0
    time = 0

    while i < len(code1) :
        time += min(abs(letter.find(code1[i])-letter.find(code2[i])),\
            abs(letter.find(code1[i])-letter.find(code2[i])-26),
            abs(letter.find(code1[i])-letter.find(code2[i])+26))
        i += 1
    print(time)
main()
