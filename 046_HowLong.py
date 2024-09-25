"HowLong"
def main() :
    "main"
    x = int(input())
    n = 0
    if x < 0 :
        x *= -1
    x = str(x)
    for _ in x :
        n += 1
    print(n)
main()
