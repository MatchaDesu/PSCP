"ชีวะจักรโบราณ"
def main() :
    "main"
    gurongi = {
        0 : "zezeso",
        1 : "papan",
        2 : "dogugu",
        3 : "gushigi",
        4 : "zugogo",
        5 : "zugagi",
        6 : "gibugu",
        7 : "gezun",
        8 : "gegido",
        9 : "bagin",
    }

    summation = 0
    num_list = []
    step = 0
    translated = ""
    num = int(input())

    if num <= 9 :
        print(gurongi[num])
        return

    while num > 9 :
        step += 1
        num, remain = divmod(num, 9)

        if step == 1 :
            summation = remain
        else :
            num_list.insert(0,[9]*(step-1)+[remain])

        if num <= 9 :
            num_list.insert(0,[9]*(step)+[num])

    num_list = list(filter(lambda x : x[-1], num_list ))

    for i, char in enumerate(num_list) :

        char = list(map(str, char))
        char = "x".join(char)
        char = char.replace("x1","")
        translated += char

        if i < len(num_list)-1 :
            translated += "+"

    text = translated+f"+{summation}"*bool(summation)
    gurongi_text = ""

    for i in text :
        if i.isnumeric() :
            gurongi_text += gurongi[int(i)]
        elif i in "x" :
            gurongi_text += "gu "
        elif i in "+" :
            gurongi_text += "do "

    print(gurongi_text.strip())
main()
