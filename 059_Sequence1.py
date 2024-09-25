"Sequence I"
def main(n) :
    "main"
    for _ in range(n) :
        for i in range(1,n+1) :
            if i == n :
                print(i)
            else :
                print(i,end=" ")
main(int(input()))
