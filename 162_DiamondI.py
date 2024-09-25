"Dimond I"
def main() :
    "main"
    diamond = []
    m = int(input())
    n = int(input())
    total = 0
    most = 0
    for _ in range(m) :
        diamond.append(list(map(int , input().split())))
    for i in range(n) :
        for j in range(m) :
            total += (diamond[j][i])
        if total > most :
            most = total
        total = 0
    print(most)
main()
