"Guess"
def clearing(num_list,do_not_need) :
    "clearing num that not included"
    for i in do_not_need :
        if i in num_list :
            num_list.remove(i)
    return num_list

def main() :
    "main"
    start = 0
    stop = 100
    not_equal = []
    while True :
        action = input()
        if action == "END" :
            break
        op,num,confirm = action.split()
        num = int(num)
        if op == '>':
            if confirm == 'YES':
                start = max(start, num + 1)
            else:
                stop = min(stop, num)
        elif op == '<':
            if confirm == 'YES':
                stop = min(stop, num - 1)
            else:
                start = max(start, num)
        elif op == '=':
            if confirm == 'YES':
                start = stop = num
            else:
                not_equal.append(num)

    print(*clearing(list(range(start, stop + 1)),not_equal))
main()
