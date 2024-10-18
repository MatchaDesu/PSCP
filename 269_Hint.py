"Hint"
def slicing(op_list) :
    "slicing list"
    num_list = list(range(10))
    op, num = op_list.split()
    num = int(num)
    if op == "==" :
        return [num]
    if op == ">" :
        return num_list[num+1:]
    if op == ">=" :
        return num_list[num:]
    if op == "<" :
        return num_list[:num]
    if op == "<=" :
        return num_list[:num+1]
    return num_list[:num] + num_list[num+1:]

def main() :
    "main"
    digit3 = slicing(input())
    digit2 = slicing(input())
    digit1 = slicing(input())

    for i in digit1 :
        for j in digit2 :
            for k in digit3 :
                print(i,j,k,sep="")
main()
