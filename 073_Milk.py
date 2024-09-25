"Milk"
def main():
    "main"
    price = float(input())
    promotion = int(input())
    free = int(input())
    money = float(input())

    bottle = int(money // price)
    caps = bottle
    if not promotion:
        print(bottle)
        return #ถ้าไม่มีโปรโมชั่นให้คืนค่าได้เลย

    while caps >= promotion:
        pro, remind = divmod(caps, promotion)
        remind += pro * free
        bottle += pro * free
        caps = remind
    print(bottle)
main()
