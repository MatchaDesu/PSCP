"Gram_v1"
def main() :
    "main"
    text = input()
    counted = {}

    for i in range(1,len(text)) :
        counted[text[i-1] + text[i]] = counted.get(text[i-1] + text[i],0) + 1

    x = list(filter(lambda x : x[1] == max(list(counted.values())), list(counted.items())))
    print(*x[0],sep="\n")

main()
