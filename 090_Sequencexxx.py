"Sequence X"
def main() :
    "main"
    size = int(input())
    amount = int(input())
    middle = (size//2) + 1
    mid_space = size-4
    side_space = 0
    for i in range(1,size+1) :
        if i in (1,size) :
            print((("*"*size+" ")*amount).strip())
        elif i < middle :
            print((("*"+" "*side_space+"*"+" "*(mid_space)+"*"+" "*side_space+"* ")*amount).strip())
            side_space += 1
            mid_space -= 2
        elif i == middle :
            print((("*"+" "*side_space+"*"+" "*side_space+"* ")*amount).strip())
            side_space -= 1
            mid_space += 2
        elif i > middle :
            print((("*"+" "*side_space+"*"+" "*(mid_space)+"*"+" "*side_space+"* ")*amount).strip())
            side_space -= 1
            mid_space += 2
main()
