"CuteCat CuteFox"
def ordering(x) :
    "Return value of list"
    if "Cat" in x[1] :
        return (1,int(x[1][3:]))
    return (2,int(x[1][3:]))

def main() :
    "main"
    name = {}
    x = None
    cat, fox = 0, 0

    for _ in range(int(input())) :
        x = input().replace("{","").replace("}","")
        name_key,name_values = x.split(" : ")
        name_key = name_key[1:-1]
        name_values = name_values[1:-1]

        if "Cat" in name_values :
            cat += 1
        else :
            fox += 1

        name.update({name_key : name_values})

    if "Cat01" not in list(name.values()) :
        if "Garfield" not in list(name) :
            cat += 1
        name.setdefault("Garfield","Cat01")

    if "Fox01" not in list(name.values()) :
        if "Fubuki" not in list(name) :
            fox += 1
        name.setdefault("Fubuki","Fox01")

    name = dict(sorted(name.items(),key=ordering))
    print("Cat",":",cat)
    print("Fox",":",fox)

    for i,y in name.items() :
        print(i,":",y)
main()
