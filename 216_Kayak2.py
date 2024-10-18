"Kayak2"
from math import inf

def main():
    "main"
    people = int(input())*2
    list_w = list(map(int, input().split()))
    total_diff, min_diff = 0, inf
    diff_list = []

    list_w.sort()

    for i in range(people) :
        for j in range(i+1,people) :
            total_diff = 0
            remain = list_w[:i] + list_w[i+1:j] + list_w[j+1:]

            total_diff = sum(list(map(lambda x, y:abs(x-y),remain[0::2], remain[1::2])))
            if total_diff < min_diff :
                min_diff = min(total_diff,min_diff)

    print(min_diff)
main()
