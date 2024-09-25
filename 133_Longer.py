"Longer"
import math

def main() :
    "main"
    circle = 2*math.pi*float(input())
    rectangle = 2*float(input())+2*float(input())
    print("Circle is longer"*(circle > rectangle)+\
        "Rectangle is longer"*(circle < rectangle)+\
        "Equal"*(circle == rectangle))
    print(f"{abs(circle-rectangle):.5f}")
main()
