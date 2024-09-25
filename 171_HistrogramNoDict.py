"Easy Histogram No Dict"
def lower(x) :
    "return value of ascii code for sorting purpose"
    if x.islower() :
        return ord(x.upper()) - 0.5
    return ord(x)

def main() :
    "main"
    text = [x for x in input() if x != " "]
    text.sort(key=lower)
    checked = []

    for i in text :
        if i not in checked :
            checked.append(i)
            print(i,"=",text.count(i))

main()
