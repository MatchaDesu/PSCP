"Niwarn"
import math

def x(n) :
    "x"
    ans = 2+(math.log(n**2, 2)/(2*n*math.log(n,2)))
    return ans

def y(n,s) :
    "y"
    ans = (math.sin(math.radians(30))+math.sqrt(2*s)) \
        / (x(n)+3)
    return ans

def z(k) :
    "z"
    ans = y(k,k)**2 + (8456*(x(k)**4)/(24*k))
    return ans

def main() :
    "main"
    n = float(input())
    s = float(input())
    k = float(input())
    print(f"X: {x(n):.1f}, Y: {y(n,s):.1f}, Z: {z(k):.1f}")
main()
