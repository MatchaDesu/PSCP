"Sequence III"
def main() :
    "main"
    x = int(input())
    for i in range(1,x+1) :
        for y in range(i,i+x) :
            if y == i+x-1 :
                print(y+1)
            else :
                print(y+1,end=" ")
main()
