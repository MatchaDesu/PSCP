"Diamond II"
def main() :
    "main"
    m, n = int(input()), int(input())
    cave = []

    for _ in range(m) :
        cave.append(list(map(int, ("0 "+input()+" 0").split())))

    for i in range(m-2,-1,-1) :
        for j in range(1,n+1) :
            cave[i][j] = max(cave[i+1][j-1]+cave[i][j],cave[i+1][j]+cave[i][j],\
                cave[i+1][j+1]+cave[i][j])

    print(max(cave[0]))
main()
