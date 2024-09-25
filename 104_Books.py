"Books"
import math

def main() :
    "main"
    amount = int(input())
    pages = int(input())
    x,y = int(input()),int(input())
    total = 0
    day = 0
    read = 0
    while read < amount :

        total += math.ceil((x/y)*pages)

        if math.ceil((x/y)*pages) >= pages :
            break
        day += 1

        if total >= pages :
            read += 1
            total = 0

        x += 1
        y += 1
    print(amount-read+day)

main()
