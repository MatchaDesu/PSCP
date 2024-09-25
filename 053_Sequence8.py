"Sequence VIII"
def main() :
    "main"
    row = int(input())
    line = ""
    for i in range(1,row+1) :
        for j in range(1,i+1) :
            if j == i :
                line += f"{j:>02}"
            else :
                line += f"{j:>02} "
        print(f"{line:>{row*3-1}}")
        line = ""
main()
