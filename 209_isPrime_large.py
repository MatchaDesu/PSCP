"isPrime_large"
from math import sqrt ,floor
def main() :
    "main"
    x = int(input())

    if x <= 1 :
        print("NO")
        return

    for i in range(2, floor(sqrt(x))+1) :
        if not x % i :
            print("NO")
            return

    print("YES")
main()
