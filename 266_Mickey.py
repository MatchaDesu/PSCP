"Mickey"
def main() :
    "main"
    n = int(input())
    mouse = []
    hole = []
    time = 0

    for _ in range(n) :
        mouse.append(int(input()))

    for _ in range(n) :
        hole.append(int(input()))

    mouse.sort()
    hole.sort()

    #print(mouse)
    #print(hole)

    for i in range(n) :
        if abs(mouse[i] - hole[i]) > time :
            time = abs(mouse[i] - hole[i])

    print(time)
main()
