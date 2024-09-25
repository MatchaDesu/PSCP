"3nPlus1"
def plus(num,num_list=None) :
    "Return num"
    if not num_list :
        num_list = []
    if num == 1 :
        return num_list
    if not num % 2 :
        num /= 2
    elif num % 2 :
        num = num*3 + 1

    num_list.append(int(num))
    return plus(num, num_list)

def main() :
    "main"
    while True :
        num = int(input())
        if not num :
            break
        total = len(plus(num)) + 1
        print(total)
main()
