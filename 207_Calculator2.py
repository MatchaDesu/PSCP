"Calculator V2"
def main():
    "main"
    n = int(input())
    base = len(str(n))
    total = 0

    if n == 1 :
        print(1)
        return

    total += n

    for i in range(1,base+1) :
        if i == base :
            total += n*(i)
        else :
            total += 9*(10**(i-1))*i
            n -= 9*(10**(i-1))
    print(total)
main()
