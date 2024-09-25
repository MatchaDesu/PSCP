"PhoneNumber"
def dom(number) :
    "Turn number into Domestic"
    msg = ""
    if len(number) < 10 :
        for i,char in enumerate(number) :
            if i in (1,5) :
                msg += f" {char}"
            else :
                msg += char
    else :
        for i,char in enumerate(number) :
            if i in (2,6) :
                msg += f" {char}"
            else :
                msg += char
    return msg

def inter(number) :
    "Turn number into International"
    msg = "+66"
    if len(number) < 10 :
        for i,char in enumerate(number[1:]) :
            if i in (0,4) :
                msg += f" {char}"
            else :
                msg += char
    else :
        for i,char in enumerate(number[1:]) :
            if i in (1,5) :
                msg += f" {char}"
            else :
                msg += char
    return msg

def main() :
    "main"
    number = str(input())
    tol = input()
    if tol == "Domestic" :
        print(dom(number))

    if tol == "International" :
        print(inter(number))
main()
    