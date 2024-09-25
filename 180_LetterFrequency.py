"LetterFrequency"
def main() :
    "main"
    text = input().lower().replace(" ","")
    most = 0
    letter = ""
    checked = ""
    for i in text :
        if i not in checked :
            checked += i

            if text.count(i) > most :
                most = text.count(i)
                letter = i
    print(letter)
main()
