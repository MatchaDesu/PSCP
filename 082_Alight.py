"Alight"
from math import ceil
def main() :
    "main"
    size = int(input())
    alight = input()
    msg = input()
    if alight == "left" :
        print(f"{msg:<{size}}")
    elif alight == "right" :
        print(f"{msg:>{size}}")
    elif alight == "center" :
        print(" "*(ceil((size-len(msg))/2)),msg," "*((size-len(msg))//2),sep="")
main()
