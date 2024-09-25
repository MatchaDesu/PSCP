"Quadrant"
def main() :
    "main"
    x = int(input())
    y = int(input())
    if not x and not y :
        print("O")
    elif x and not y :
        print("X")
    elif not x and y :
        print("Y")
    elif x > 0 :
        if y > 0 :
            print("Q1")
        elif y < 0 :
            print("Q4")
    elif x < 0 :
        if y > 0 :
            print("Q2")
        elif y < 0 :
            print("Q3")
main()
