"Duplicate I"
def main() :
    "main"
    set_a = set()
    set_b = set()
    a,b = int(input()),int(input())

    for _ in range(a) :
        set_a.add(int(input()))

    for _ in range(b) :
        set_b.add(int(input()))

    num = list(map(str,sorted(set_a.intersection(set_b),reverse=True)))

    if num :
        for i in num :
            print(i)
    else :
        print("Nope")
main()
