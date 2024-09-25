"Ball"
def main() :
    "main"
    height = float(input())
    count = 0
    while height >= 0.01 :
        height *= 3/5
        if height >= 0.01 :
            count += 1
    print(count)
main()
