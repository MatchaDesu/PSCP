"Matrix_MN"
def main() :
    "main"
    m = int(input())
    n = int(input())
    count = 0

    for _ in range(m*n) :
        count += 1
        print(input(),end=" ")
        if count == n :
            print()
            count = 0

main()
