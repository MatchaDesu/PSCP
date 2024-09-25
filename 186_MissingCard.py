"MissingCard"
def main() :
    "main"
    rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    symbal = ["S","H","D","C"]
    all_cards = set()
    find_card = set()

    for i in symbal :
        for j in rank :
            all_cards.add(f"{j}{i}")

    for _ in range(51) :
        find_card.add(input())

    print("".join(all_cards-find_card))

main()
