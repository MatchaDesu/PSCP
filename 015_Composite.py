"Composite"
def f(x) :
    "f funtion"
    ans = 2 * x
    return ans

def g(x) :
    "g funtion"
    ans = (x / 2) + 1
    return ans

def main() :
    "main"
    x = int(input())
    print(f"{f(g(x)):.2f}")
    print(f"{g(f(x)):.2f}")
main()
