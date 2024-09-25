"US Interstate Number System"
def main() :
    "main"
    road = f"{input():>03}"

    #Check that number is in range or not
    if not (5 <= int(road[1:]) <= 95) or int(road[1:]) % 5 :
        print("Others")
        return

    #Minor Road
    if not int(road[0]) % 2 and int(road[0]) > 0 :
        print("Even Minor Interstate")
        print(f"I-{int(road[1:])}")
        return
    if int(road[0]) % 2 and int(road[0]) > 0 :
        print("Odd Minor Interstate")
        print(f"I-{int(road[1:])}")
        return

    #Major Road
    if road[-1] in "0" :
        print("Horizontal Major Interstate")
        print(f"I-{int(road[1:])}")
        return
    if road[-1] in "5" :
        print("Vertical Major Interstate")
        print(f"I-{int(road[1:])}")
        return

main()
