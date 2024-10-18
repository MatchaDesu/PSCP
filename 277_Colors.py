"Colors"
def main() :
    "main"
    x = input()
    y = input()

    if x == y and x in ("Red","Blue","Yellow"):
        print(x)

    elif ["Red","Yellow"] in ([x,y],[y,x]) :
        print("Orange")

    elif ["Blue","Yellow"] in ([x,y],[y,x]) :
        print("Green")

    elif ["Red","Blue"] in ([x,y],[y,x]) :
        print("Violet")

    else :
        print("Error")
main()
