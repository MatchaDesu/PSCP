"Olympic"
def main() :
    "main"
    part = int(input())
    player = {}
    country, medals = None, None
    current_score = []
    place,current_place = 0, 0

    for _ in range(part) :
        text = input()
        country = text.split()[0]
        medals = list(map(int, text.split()[1:]))
        player.update({country : medals})
    player = sorted(player.items(),key=lambda x : x[1],reverse=True)

    for i, _ in enumerate(player) :
        for j in range(i) :
            if player[j][1] == player[i][1] and player[j][0] > player[i][0]:
                player[j],player[i] = player[i],player[j]
    player = dict(player)

    for i,j in player.items() :
        current_place += 1
        if j != current_score :
            current_score = j
            place = current_place
            print(current_place,end=" ")
        else :
            print(place,end=" ")

        print(i," ".join(map(str,j)),sum(j))
main()
