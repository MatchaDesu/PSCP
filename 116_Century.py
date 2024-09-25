"Century"
from math import ceil
def main() :
    "main"
    num = int(input())
    for _ in range(num) :
        year = input()
        year_num = int(year[5:])
        if year[:4] in "B.E." :
            year_num -= 543
        if year_num <= 0 :
            print("ERROR")
        else :
            year_num = ceil(year_num / 100)
            print(year_num)
main()
