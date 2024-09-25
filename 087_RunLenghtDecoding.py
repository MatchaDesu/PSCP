"Run Lenght Decoding"
def main() :
    "main"
    decimal_number = "0123456789"
    msg = input()
    number = ""
    letter = ""
    for i in msg :
        if i in decimal_number :
            number += i
        else :
            letter += i
            print(letter*int(number),end="")
            letter,number = "",""
main()
