"Milk v2"
def main() :
    "main"
    price = float(input())
    caps = int(input())
    bonus_caps = int(input())
    bottles = int(input())
    bonus_bottles = int(input())
    money = float(input())
    total_caps = total_bottle = total = money // price

    while True :
        if total_caps < caps and total_bottle < bottles :
            break
        if total_caps >= caps :
            total_caps -= caps
            total_caps += bonus_caps
            total_bottle += bonus_caps
            total += bonus_caps
        if total_bottle >= bottles :
            total_bottle -= bottles
            total_caps += bonus_bottles
            total_bottle += bonus_bottles
            total += bonus_bottles
    print(int(total))
main()
