"Sequence N"
def main() :
    "main"
    height = int(input())
    for i in range(1,height+1) :
        for j in range(1,height+1) :
            if j in (1,i,height) :
                print("*",end="")
            else :
                print(" ",end="")
        print()
main()
