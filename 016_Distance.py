"Distance"
def d(q,p) :
    "d"
    ans = (q - p)**2
    return ans

def main() :
    "main"
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    print((d(q1,p1) + d(q2,p2))**(1/2))
main()
