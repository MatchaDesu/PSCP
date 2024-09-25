"PIC"
import math

def main():
    "main"
    x = int(input())
    y = int(input())
    r = int(input())
    xn = int(input())
    yn = int(input())
    d = math.dist((x,y),(xn,yn))
    if d > r :
        print("False")
    else :
        print("True")
main()
