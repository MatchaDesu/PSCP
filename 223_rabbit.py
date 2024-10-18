"Rabbit"
def main() :
    "main"
    rabbits = int(input())
    jumps = int(input())
    carrots = int(input())
    overload = 0
    shorten = False

    n = min(rabbits,carrots)

    if (n/2)*(n+1) > jumps :
        n = int((-1 + (1+8*jumps)**0.5)/2)
        overload = min(rabbits,carrots) - n
        shorten = True

    sequence = int((n/2)*(n+1))

    jump_not_carrot = jumps - sequence
    remain_rabbits = max(rabbits-carrots,0) + overload
    remain_carrots = max(carrots-rabbits,0) + overload

    if not remain_carrots + remain_rabbits + jump_not_carrot:
        print("Ahhahaha")
        return

    if  not (remain_carrots + remain_rabbits) and jump_not_carrot and shorten:
        print("Ahhahaha")
        return

    print(remain_rabbits,jump_not_carrot,remain_carrots)

main()
