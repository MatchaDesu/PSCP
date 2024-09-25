"Tug of War"
def main(counta = 0,countb = 0) :
    "main"
    for _ in range(10) :
        counta += int(input())
    for _ in range(10) :
        countb += int(input())
    print("A"*(countb>=counta)+"B"*(counta>=countb))
main()
