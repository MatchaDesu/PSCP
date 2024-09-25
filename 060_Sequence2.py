"Sequence II"
def main(n) :
    "main"
    for i in range(1,n+1) :
        print(i**2,end="")
        if i < n :
            print(end=" ")
main(int(input()))
