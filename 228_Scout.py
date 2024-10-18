"Scout"
def main() :
    "main"
    for _ in range(int(input())) :

        p,q,r = map(int, input().split())
        egg = list(map(int, input().split()))
        total_weight = 0
        total_egg = 0
        total = 0

        egg.sort()

        for i in range(p) :

            total_egg += 1
            total_weight += egg[i]

            if total_egg > q or total_weight > r :
                break
            total += 1
        print(total)

main()
