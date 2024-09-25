"Christmas Tree"
def main() :
    "main"
    leaves = int(input())
    trunk = int(input())
    start = leaves
    for i in range(1,leaves+1) :
        x = "*"*(i*2-1)
        print(f"{x:>{start+i-1}}")
    for i in range(1,trunk+1) :
        y = "---"
        print(f"{y:>{leaves+1}}")
main()
