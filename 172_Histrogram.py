"Easy Histogram"
def lower(x) :
    "return value of ascii code for sorting purpose"
    if x.islower() :
        return ord(x.upper()) - 0.5
    return ord(x)

def main() :
    "main"
    text = [x for x in input() if x != " "]
    text.sort(key=lower)
    check = dict.fromkeys(text,0)

    for i in text :
        check[i] += 1

    for i,y in dict.items(check) :
        print(i,"=",y)
main()
