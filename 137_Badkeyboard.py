"Bad Keyboard"
def main() :
    "main"
    word = input()
    new_word = ""
    for i in word :
        if i in "i" :
            new_word += "o"
        elif i in "I" :
            new_word += "O"
        elif i in "o" :
            new_word += "i"
        elif i in "O" :
            new_word += "I"
        else :
            new_word += i
    print(new_word)
main()
