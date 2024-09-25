"CaesarV2"
def caesar(letter,num) :
    "Return letter"
    new_text = ""

    for i in letter :
        if i.isalpha() :
            if ord(i.upper()) + num < 65 :
                i = chr(ord(i) + num + 26)
            elif ord(i.upper()) + num > 90 :
                i = chr(ord(i) + num - 26)
            else :
                i = chr(ord(i) + num)
            new_text += i

    return new_text.lower()

def find_rotate(text) :
    "return how many times to rotate"
    word = ["what", "when", "why", "which", "this", "there", "where", "the", "is", "am", "are",\
         "you", "we", "they", "he", "she", "it"]
    text = text.split()

    for i in text :
        for num in range(1,26) :
            if caesar(i,num) in word :
                return num

    return 0

def main() :
    "main"
    text = input()
    num = find_rotate(text)
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
