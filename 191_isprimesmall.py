"IsPrimeSmall"
from math import sqrt ,floor
def main() :
    "main"
    x = int(input())

    if x <= 1 :
        print("No")
        return

    for i in range(2, floor(sqrt(x))+1) :
        if not x % i :
            print("No")
            return

    print("Yes")
main()
