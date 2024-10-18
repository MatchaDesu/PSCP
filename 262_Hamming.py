"[Final 2019] Hamming"
def main() :
    "main"
    a = input()
    b = input()
    n = len(a)
    count = 0
    for i in range(n) :
        if not a[i] == b[i] :
            count += 1
    print(count)
main()
