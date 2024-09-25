"Sequence IV"
def main() :
    "main"
    x = int(input())
    for i in range(1,x+1) :
        for y in range(1,x+1) :
            if y == x :
                print(((i-1)*x)+y)
            else :
                print(((i-1)*x)+y,end=" ")
main()
