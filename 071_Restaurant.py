"Restaurant"
def main() :
    "main"
    food_price = float(input())
    promotion = float(input())
    discount = (100 - float(input())) / 100
    recommand = float(input())
    total = (food_price + recommand)*discount

    if food_price >= promotion :
        food_price *= discount

    if discount < 1 :
        if total > food_price :
            print(f"No {total-food_price:.3f}")
        elif total == food_price :
            print("Yes")
        else :
            print(f"Yes {food_price-total:.3f}")
    else :
        print("Yes")
main()
