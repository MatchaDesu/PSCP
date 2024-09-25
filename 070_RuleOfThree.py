"Rule of Three"
def main() :
    "main"
    number = int(input())
    price,weight = [],[]
    valuable = 0
    set_of_snack = 0
    for _ in range(number) :
        price.append(float(input()))
        weight.append(float(input()))
    for i in range(number) :
        if weight[i] / price[i] > valuable :
            valuable = weight[i] / price[i]
            set_of_snack = i
        elif  weight[i] / price[i] == valuable :
            if price[i] <= price[set_of_snack] :
                valuable = weight[i] / price[i]
                set_of_snack = i
    print(f"{price[set_of_snack]:.2f} {weight[set_of_snack]:.2f}")
main()
