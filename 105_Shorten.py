"Shorten"
def main() :
    "main"
    num = 0
    current = num
    start = num
    stop = num
    shorten = ""

    while num != -1 :
        num = int(input())
        if num != -1 :
            if not start :
                start = num
                current = num
            if num - current > 1 :
                shorten += f"{start}"+f"-{stop}"*bool(stop-start)+", "
                start = num
                stop = num
            else :
                stop = num
            current = num
        else :
            if start and stop and current :
                shorten += f"{start}"+f"-{stop}"*bool(stop-start)
                print(shorten)
main()
