"Distribute"
def main():
    "main"
    money = int(input())
    people = int(input())

    if money < people or (money == 4 and people == 1) :
        print(-1)
        return

    if people*8 < money :
        print(people-1)
        return

    money -= people
    eight, remain = divmod(money,7)
    remain_child = people - eight

    if remain == 3 and remain_child <= 1 :
        eight -= 1
    print(eight)

main()
