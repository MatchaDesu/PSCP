"Point Sorting"
def f(position) :
    "return x + y"
    x = int(position[0])
    y = int(position[1])
    return x+y

def ordering(pos) :
    "Ordering if same value"
    for i ,_ in enumerate(pos) :
        for y in range(i) :
            if int(pos[i][0])+int(pos[i][1]) == int(pos[y][0])+int(pos[y][1]) and \
                int(pos[i][1]) > int(pos[y][1]) :
                pos[i], pos[y] = pos[y], pos[i]
    return pos

def main() :
    "main"
    point = []
    for _ in range(int(input())) :

        for _ in range(int(input())) :
            point.append(input().split())
        point.sort(key=f)
        ordering(point)

        for i in point :
            print(" ".join(i))
        point.clear()

main()
