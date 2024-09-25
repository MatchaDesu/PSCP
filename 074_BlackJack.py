"Black Jack"
def main() :
    "main"
    spacial = "J","Q","K"
    cards = int(input())
    score = 0
    hand = ""

    for _ in range(cards) :
        in_hand = input()
        hand += in_hand
        if in_hand in spacial :
            score += 10
        elif in_hand == "A" :
            score += 11
        else :
            score += int(in_hand)

    count = hand.count("A")

    while score > 21 and count > 0 :
        score -= 10
        count -= 1

    print(score)
main()
