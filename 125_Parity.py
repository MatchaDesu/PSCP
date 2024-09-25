"Parity"
def main() :
    "main"
    bits = str(input())
    x = input()
    one_bit = 0
    for i in bits :
        if i in "1" :
            one_bit += 1

    if not one_bit % 2 or not one_bit :
        if x == "Odd" :
            bits += "1"
        else :
            bits += "0"
    else :
        if x == "Odd" :
            bits += "0"
        else :
            bits += "1"
    print(bits)
main()
