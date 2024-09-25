"Coprime V1"
def main() :
    "main"
    num1 = int(input())
    num2 = int(input())
    base = 2
    total = 1

    if min(num1, num2) <= 0 :
        print(max(num1,num2))
        return

    while True :
        if base > min(num1, num2) :
            break
        if not (num1 % base  or num2 % base) :
            num1 /= base
            num2 /= base
            total *= base
        else :
            base += 1

    if total == 1 :
        print("YES")
    else :
        print("NO")
    print(total)
main()
