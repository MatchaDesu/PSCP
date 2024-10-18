"Dart"
def main() :
    "main"
    dart = int(input())
    total = 0

    for _ in range(dart) :
        x,y = map(int, input().split())
        distance = (x**2 + y**2)**0.5

        if distance <= 2 :
            total += 5
        elif distance <= 4 :
            total += 4
        elif distance <= 6 :
            total += 3
        elif distance <= 8 :
            total += 2
        elif distance <= 10 :
            total += 1

    print(total)
main()
