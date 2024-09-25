"bonus"
def main() :
    "main"
    money = int(input())
    year = int(input())
    month = int(input())

    if month >= 10 :
        year += 1

    if year >= 20 :
        year = 20

    money *= year

    if money < 5000 :
        money = 5000
    elif money > 1_000_000 :
        money = 1_000_000

    print(money)
main()
