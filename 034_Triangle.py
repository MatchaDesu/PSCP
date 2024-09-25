"Triangle"
def main() :
    "main"
    a = float(input())
    b = float(input())
    c = float(input())
    phy_a = (b**2 + c**2)**0.5
    phy_b = (a**2 + c**2)**0.5
    phy_c = (a**2 + b**2)**0.5
    if abs(phy_a-a) <= 0.01 :
        print("Yes")
    elif abs(phy_b-b) <= 0.01 :
        print("Yes")
    elif abs(phy_c-c) <= 0.01 :
        print("Yes")
    else :
        print("No")
main()
