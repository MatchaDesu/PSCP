"Geade II"
def main() :
    "main"
    x = float(input())
    if 95 <= x <= 100 :
        print("A")
    elif 90 <= x < 95 :
        print("B+")
    elif 85 <= x < 90 :
        print("B")
    elif 80 <= x < 85 :
        print("C+")
    elif 75 <= x < 80 :
        print("C")
    elif 70 <= x < 75 :
        print("D+")
    elif 65 <= x < 70 :
        print("D")
    elif 60 <= x < 65 :
        print("F+")
    elif 0 <= x < 60 :
        print("F")
    else :
        print("ERR")
main()
