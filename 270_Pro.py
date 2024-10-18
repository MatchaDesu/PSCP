"Pro"
def main() :
    "main"
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())

    pro, remain = divmod(z,x)
    total = pro*y*a + remain*a
    print(total)
main()
