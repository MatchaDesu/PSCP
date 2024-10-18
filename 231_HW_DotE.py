"HW_DotE"
from math import factorial

def main() :
    "main"
    n = int(input())

    if n == 1 :
        n = 2

    r =  n // 2

    combination = int(factorial(n)/(factorial(r)*factorial(n-r)))

    if n % 2 :
        combination *= 2

    print(combination)
main()
