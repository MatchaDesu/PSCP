"Regulation"
def main() :
    "main"
    a = int(input())
    b = float(input())
    c = str(input())
    print(f"{a:>30}")
    if a < 0 :
        a *= -1
        print(f"-{a:>029}")
    else :
        print(f"{a:>030}")
    print(f"{b:.2f}")
    print(f"{b:.12f}")
    print(f"{c:>40}")
main()
