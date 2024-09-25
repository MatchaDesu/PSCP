"BreachTheDoor"
def letter_6(word) :
    """Return word if len more than 6
    Return None Otherwise"""
    new_word = ""
    for i in word :
        if not i.isnumeric() and i.isalpha() :
            new_word += i
    if len(new_word) > 6 :
        return new_word
    return ""

def main() :
    "main"
    paragraph = str(input())
    paragraph = paragraph.split()
    paragraph = list(map(letter_6, paragraph))
    password = " ".join(paragraph).split()
    print(" ".join(password))
main()
