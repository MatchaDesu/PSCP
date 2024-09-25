"Pick Them"
import json
def main() :
    "main"
    x = json.loads(str(input()))
    even = []

    for i in x :
        if not i % 2 :
            even.append(i)

    if even :
        for i in even :
            print(i)
    else :
        print("Nope")
main()
