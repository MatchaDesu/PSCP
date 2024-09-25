"MissingNumber"
def main() :
    "main"
    set_a = set()
    set_b = set()

    for i in range(1,int(input())+1) :
        set_a.add(i)

    while True :
        num = int(input())
        if not num :
            break
        set_b.add(num)

    lost = sorted(set_a-set_b)

    for i in lost :
        print(i)

main()
