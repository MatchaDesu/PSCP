"7 Segments Simulator"
def to_num(binary) :
    """input 0 or 1 eight times
    and return number that show on screen
    ***Error if can't show***"""
    num = ""
    if binary == "1111110" :
        num = "0"
    if binary == "0110000" :
        num = "1"
    if binary == "1101101" :
        num = "2"
    if binary == "1111001" :
        num = "3"
    if binary == "0110011" :
        num = "4"
    if binary == "1011011" :
        num = "5"
    if binary == "1011111" :
        num = "6"
    if binary == "1110000" :
        num = "7"
    if binary == "1111111" :
        num = "8"
    if binary == "1111011" :
        num = "9"
    if num :
        return num
    return "Error"

def main() :
    "main"
    binary = ""
    screen = ""
    for _ in range(3) :
        for _ in range(7) :
            if input() in "on" :
                binary += "1"
            else :
                binary += "0"
        screen += to_num(binary)
        if input() in "on" :
            screen += "."
        binary = ""

    if screen.count(".") > 1 or "Error" in screen :
        print("Error")
        return

    print(f"{float(screen):.2f}")
main()
