"AndAgain"
def vowel(text) :
    "Checked if text has 2+ vowel"
    count = 0
    for i in text :
        if i in "aeiou" :
            count += 1
    if count >= 2 :
        return True
    return False

def main() :
    "main"
    text = input().replace(".","").split()
    text_pass = list(filter(vowel, text))
    text_pass.sort()
    if text_pass :
        for i in text_pass :
            print(i)
    else :
        print("Nope")
main()
