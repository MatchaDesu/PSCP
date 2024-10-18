"Difference"
from collections import Counter
from json import loads

def difference(list_a,list_b) :
    """
    return Value after find diff
    """
    counted = []
    for i in list_a.keys() :
        list_a[i] -= list_b.get(i,0)
        list_a[i] = abs(list_a[i])
        counted.append(i)

    for i in list_b.keys() :
        if i not in counted :
            list_b[i] -= list_a.get(i,0)
        else :
            list_b[i] = 0

    return list_a,list_b

def main() :
    "main"
    list_a = Counter(loads(input()))
    list_b = Counter(loads(input()))

    diff = difference(list_a,list_b)
    diff = list(filter(lambda x : x[1] > 0,diff[0].items())) + \
            list(filter(lambda x : x[1] > 0,diff[1].items()))

    diff.sort()

    if diff :
        for i in diff :
            print(*i)
    else :
        print("ONAJI DAYO!")
main()
