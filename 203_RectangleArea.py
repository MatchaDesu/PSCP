"RectangleArea"
def main() :
    "main"
    x1,y1,w1,h1 = list(map(int,input().split()))
    x2,y2,w2,h2 = list(map(int,input().split()))

    x_point = max(0, min(x1+w1,x2+w2) - max(x1,x2))
    y_point = max(0, min(y1+h1,y2+h2) - max(y1,y2))

    if x_point*y_point :
        print(x_point*y_point)
    else :
        print("no overlapping")
main()
