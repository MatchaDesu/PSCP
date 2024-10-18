"Lucky Number"
def main() :
    "main"
    num = list(range(1,int(input())+1,2))
    index = 1
    temp = num.copy()

    while len(num) > index :
        for i in range(num[index]-1,len(num),num[index]) :
            temp.remove(num[i])
        num = temp.copy()
        index += 1

    print(*num)
main()
