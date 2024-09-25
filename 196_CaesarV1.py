"CaesarV1"
def main() :
    "main"
    num = int(input()) % 26
    text = input()
    new_text = ""

    for i in text :
        if i.isalpha() :

            if ord(i.upper()) + num < 65 :
                i = chr(ord(i) + num + 26)
            elif ord(i.upper()) + num > 90 :
                i = chr(ord(i) + num - 26)
            else :
                i = chr(ord(i) + num)

        new_text += i
    print(new_text)
main()
