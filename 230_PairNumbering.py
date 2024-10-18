"PairNumbering"
from json import loads

def main() :
    "main"
    a_list = list(map(int ,loads(input())))
    b_list = list(map(int ,loads(input())))
    p = int(input())
    remainder = []
    total = 0

    a_list = list(filter(lambda x : x <= p, a_list))
    b_list = list(filter(lambda x : x <= p, b_list))

    a_list.sort()
    b_list.sort()

    for num in a_list:
        if num not in remainder:
            target = p - num
            if target in b_list:
                total += a_list.count(num) * b_list.count(target)
            remainder.append(num)

    print(total)

main()
