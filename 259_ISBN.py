"ISBN"
def main() :
    "main"
    num = input().replace("-","").replace(" ","")
    num, check = num[:-1], num[-1]
    coefficient = 10
    total = 0
    for i in num :
        total += int(i)*coefficient
        coefficient -= 1

    total = -total % 11
    if total == 10 :
        total = "X"

    if str(total) == check :
        print("Yes")
    else :
        print("No",total)
main()
