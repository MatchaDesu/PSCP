"Pringles"
def main() :
    "main"
    package = input()
    inside = input()
    package = input()
    reach = int(input())
    eated = ""
    count = 0
    for i in inside :
        if reach > 0 and i == ")" :
            eated += " "
            count += 1
        else :
            eated += i
        reach -= 1
    print(count)
    if eated.count(")") > 0 :
        print("There are still some left.")
    else :
        print("None.")
    print(package,eated,package,sep="\n")
main()
