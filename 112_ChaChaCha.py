"Cha Cha Cha"
from math import ceil
def main() :
    "main"
    day = int(input())
    total = 0
    for _ in range(day) :
        total += 8720*ceil(float(input()))
    print(total)
main()
