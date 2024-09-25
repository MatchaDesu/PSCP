"Pick Them Again"
def main() :
    "main"
    num = str(input()).split()
    num.reverse()
    printable = []
    for i in num :
        if not int(i) % 3 or not int(i) % 5 :
            printable.append(i)
    if printable :
        for i in printable :
            print(i)
    else :
        print("Nope")
main()
