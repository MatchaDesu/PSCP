"SumOfNumber"
def main() :
    """ SumOfNumber """
    stop = int(input())
    x = 0
    total = 0
    while x != -1 and total != stop :
        x = int(input())
        if x != -1 :
            total += x
    print(total)
main()
