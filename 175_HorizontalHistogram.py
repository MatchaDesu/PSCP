"HorizontalHistogram"
def lower(x) :
    "lower before upper"
    x = x[0]
    if x.islower() :
        return 1,x
    return 2,x

def main() :
    "main"
    histrogram = {}
    text = str(input())
    for i in text :
        histrogram.setdefault(i,"")
        if not len(histrogram[i].replace("|","")) % 5 and histrogram[i] :
            histrogram[i] += "|"
        histrogram[i] += "-"

    histrogram = dict(sorted(histrogram.items(),key=lower))
    for i, y in histrogram.items() :
        print(i,":",y)
main()
