"PedFonFire"
from math import factorial
def main() :
    "main"
    total = 0
    ped = []
    remaider = []

    for _ in range(int(input())) :
        ped.append(int(input()))

    weight = int(input())

    for i in range(0,weight+1) :
        if i == weight-i and ped.count(i) <= 1 :
            continue
        if i == weight-i :
            total += int(factorial(ped.count(i))/(factorial(ped.count(i)-2)*2))
        elif i not in remaider :
            total += ped.count(i)*ped.count(weight-i)
            remaider.append(weight-i)

    print(total)
main()
