"Coffee Shop"
def main() :
    "main"
    price = float(input())
    disc1 = (100-float(input()))/100
    disc2 = (100-float(input()))/100
    pro = float(input())
    cups = int(input())

    #pro 1
    total1 = (price + (cups-1)*(price*disc1))*bool(cups>0)

    #pro 2
    total2 = price*cups
    if total2 >= pro :
        total2 *= disc2

    if total2 <= total1 :
        print(2)
        print(f"{total2:.2f}")
    else :
        print(1)
        print(f"{total1:.2f}")
main()
