"Indicator"
def main() :
    "main"
    lenght = int(input())
    height = int(input())
    space = (height-1)/2
    op = "minus"
    for _ in range(height) :
        print(" "*int(space),"*"*lenght,sep="")
        if space > 0 :
            if op == "minus" :
                space -= 1
            else :
                space += 1
        elif not space :
            op = "plus"
            space += 1
main()
