"Diamond"
def main() :
    "main"
    number = int(input())
    middle = (number // 2) +1
    space = 1
    for i in range(1,number+1) :
        if i in (1,number) :
            print(f"{'*':>{middle}}")
        elif i == middle :
            print("*"*number)
            space -= 1
        elif i > middle :
            print(f"{('*'+' '*(space*2-1)+'*'):>{middle+space}}")
            space -= 1
        elif i < middle :
            print(f"{('*'+' '*(space*2-1)+'*'):>{middle+space}}")
            space += 1
main()
