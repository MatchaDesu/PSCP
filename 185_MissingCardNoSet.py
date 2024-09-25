"MissingCard No Set"
def main() :
    "main"
    rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    symbal = ["S","H","D","C"]
    all_cards = []

    for i in symbal :
        for j in rank :
            all_cards.append(f"{j}{i}")

    for _ in range(51) :
        all_cards.remove(input())

    print("".join(all_cards))

main()
