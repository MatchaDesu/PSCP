"Indicator"
def main() :
    "main"
    lenght = int(input())
    height = int(input())
    space = 0
    op = "plus"
    for _ in range(height) :
        print(" "*int(space),"*"*lenght,sep="")
        if space < (height-1)/2 :
            if op == "plus" :
                space += 1
            else :
                space -= 1
        else :
            op = "minus"
            space -= 1
main()
