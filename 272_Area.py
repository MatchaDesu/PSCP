"Area"
def main() :
    "main"
    n = int(input())
    count = 0
    for _ in range(n) :
        for i in input() :
            if i not in " " :
                count += 1
    print(count)
main()
