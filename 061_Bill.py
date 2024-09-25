"bill"
def main() :
    "main"
    food_price = int(input())
    service_charge = food_price*10/100

    if service_charge < 50 :
        service_charge = 50

    elif service_charge > 1000 :
        service_charge = 1000

    vat = (food_price + service_charge)*7/100
    total = food_price + service_charge + vat
    print(f"{total:.2f}")
main()
