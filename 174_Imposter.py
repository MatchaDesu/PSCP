"Imposter"
import json

def main() :
    "main"
    alive = {}
    dead = {}
    dead_name,dead_role = None, None

    while True :
        placeholder = input()
        if placeholder in "Start" :
            break

        alive.update(json.loads(placeholder))

    alive = dict(sorted(alive.items(),key=lambda x : x[0]))

    while True :
        placeholder = input()
        if placeholder in "End" :
            break

        dead_name = placeholder
        dead_role = alive.pop(placeholder)
        dead.update({dead_name : dead_role})

    dead = dict(sorted(dead.items(),key=lambda x : x[0]))

    print(list(alive.values()).count("Impostor"),"Impostor Remains")

    print("***Alive***")
    for i,y in alive.items() :
        print(i,":",y)

    print("***Dead***")
    for i,y in dead.items() :
        print(i,":",y)

main()
