"AllPrime"
from math import sqrt ,floor

def is_prime(x) :
    "Check the number"
    for i in range(2, floor(sqrt(x))+1) :
        if not x % i :
            return 0
    return 1

def main() :
    "main"
    total = 0
    stop = int(input())
    for i in range(2,stop+1) :
        total += is_prime(i)
    print(total)
main()
