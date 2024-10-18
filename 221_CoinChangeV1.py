"CoinChangev1"
def main() :
    "main"
    money = int(input())
    total_25,remain = divmod(money,25)
    total_10,remain = divmod(remain,10)
    total_5,total_1 = divmod(remain,5)

    coin_amount = total_1 + total_5 + total_10 + total_25

    print(coin_amount)
main()
