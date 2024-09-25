"Counting Star"
def main() :
    "main"
    sky = input()
    constellation = 0
    comet = 0
    shooting_star = 0
    counting = ""
    for i in sky :
        counting += i
        if "~*" in counting :
            comet += 1
            counting = ""
        elif "*~" in counting :
            comet += 1
            counting = ""
        elif "*/" in counting :
            shooting_star += 1
            counting = ""
        elif "**" in counting :
            constellation += 1
            counting = ""
    if comet or shooting_star or constellation :
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
    else :
        print("Tonight is a quiet night.")
main()
