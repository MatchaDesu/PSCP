"isPrime_large"
def main() :
    "main"
    x = int(input())

    if x <= 1 :
        print(False)
        return

    if x == 2 :
        print(True)
        return

    if not x % 2 :
        print(False)
        return

    for i in range(3, int((x)**0.5)+1, 2) :
        if not x % i :
            print(False)
            return

    print(True)
main()
