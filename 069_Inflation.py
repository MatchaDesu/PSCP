"""inflation"""
def main():
    """inflation"""
    money = float(input())
    money = int(money*100)
    year = int(input())
    for _ in range(year):
        money += money *381//10000
    if not money:
        print("0.00")
    else:
        money = str(money)
        print(money[:-2]+"."+money[-2:])
main()
