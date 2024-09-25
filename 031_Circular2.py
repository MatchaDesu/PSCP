"Circular II"
import math

def main():
    "main"
    x = float(input())
    y = float(input())
    r = abs(float(input()))
    xn = float(input())
    yn = float(input())
    rn = abs(float(input()))
    d = math.sqrt((x-xn)**2 + (y-yn)**2)
    if d < r+rn :
        print("Yes")
    else :
        print("No")
main()
