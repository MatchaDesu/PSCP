"Kabata"
def main() :
    "main"
    language = ["bakka","ta","ba","ka"]
    text = None

    for _ in range(int(input())) :
        text = input()

        for j in language :
            if "baka" in text :
                break
            if j in text :
                text = text.replace(j," ")

        if not text.strip() :
            print("yes")
        else :
            print("no")
main()
