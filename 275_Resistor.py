"Resistor"
def main() :
    "main"
    color = {
        "Black" : [0],
        "Brown" : [1,1],
        "Red" : [2,2],
        "Orange" : [3],
        "Yellow" : [4],
        "Green" : [5,0.5],
        "Blue" : [6,0.25],
        "Purple" : [7,0.10],
        "Grey" : [8,0.05],
        "White" : [9],
        "Gold" : [-1,5],
        "Silver": [-2,10]
    }

    num1 = input()
    num2 = input()
    num3 = input()
    num4 = input()

    if num1 in ("Gold","Silver") or num1 not in color :
        print("Error")
        return

    if num2 in ("Gold","Silver") or num2 not in color :
        print("Error")
        return

    if num3 in ("Grey","White") or num3 not in color :
        print("Error")
        return

    if num4 in ("Black","Orange","Yellow","White") or num4 not in color :
        print("Error")
        return

    total = (color[num1][0]*10 + color[num2][0]) * 10**color[num3][0]
    print(f"{total*((100-color[num4][1])/100):.4f}")
    print(f"{total*((100+color[num4][1])/100):.4f}")
main()
