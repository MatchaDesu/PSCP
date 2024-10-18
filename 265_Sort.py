"Merge"
def main() :
    "main"
    num_list = []

    while True :
        num = input()
        if num == "END" :
            break
        num_list.append(int(num))

    #print(num_list)
    ans = slicing(num_list)

    print(*ans,sep="\n")

def slicing(x):
    "Slicing left and right"
    if len(x) <= 1:
        return x

    mid = len(x) // 2
    left = x[:mid]
    right = x[mid:]

    left_side = slicing(left)
    right_side = slicing(right)

    return merge(left_side, right_side)

def merge(left, right):
    "merging to list and return"
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

main()
