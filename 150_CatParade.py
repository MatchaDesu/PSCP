"Cat Parade"
def main() :
    "main"
    parade = None
    cat = []
    check = []
    checked = []

    while True :
        parade = input()
        if parade == "END" :
            break
        if parade == "IT'S A DOG" :
            cat.pop()
        else :
            parade = parade.split(", ")
            for i in parade :
                cat.append(i)

    check = cat.copy()
    check.sort()

    for i in check :
        if i not in checked :
            checked.append(i)
            print(i,cat.index(i)+1,cat.count(i))
main()
