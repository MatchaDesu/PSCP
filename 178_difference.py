"Difference"
def main() :
    "main"
    set_a = set()
    set_b = set()
    a,b = int(input()),int(input())

    for _ in range(a) :
        set_a.add(int(input()))

    for _ in range(b) :
        set_b.add(int(input()))

    num = map(str,sorted(set_a-set_b))

    print(" ".join(num))
main()
