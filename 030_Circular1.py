"Circular I"
import math

def main():
    "main"
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())
    d = math.dist((x,y),(xn,yn))
    if d > r :
        print("No")
    else :
        print("Yes")
main()
