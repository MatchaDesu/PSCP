"Post Office"
def env(x) :
    "Calculates service of envelope type"
    if x <= 10 :
        return 16+13
    if 10 < x <= 20 :
        return 18+13
    if 20 < x <= 100 :
        return 23+13
    if 100 < x <= 250 :
        return 28+13
    if 250 < x <= 500 :
        return 33+13
    if 500 < x <= 1000 :
        return 48+13
    return 68+13

def box(x) :
    "Calculates service of box type"
    if x <= 500 :
        return 45+15
    if 500 < x <= 1000 :
        return 55+15
    return 70+15

def main() :
    "main"
    envelope = int(input())
    boxes = int(input())
    total = 0
    for _ in range(envelope) :
        total += env(float(input()))

    for _ in range(boxes) :
        total += box(float(input()))

    print(total)
main()
