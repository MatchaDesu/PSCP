"Password"
import math

def main() :
    "main"
    password = str(input())
    lower = ""
    upper = ""
    number = ""
    symbol = ""
    for i in password :
        if i.islower() :
            lower += i
        elif i.isupper() :
            upper += i
        elif i.isnumeric() :
            number += i
        elif i.isprintable() :
            symbol += i
    r_total = 26*(bool(lower))+ \
            26*(bool(upper))+ \
            10*bool(number)+ \
            32*bool(symbol)
    l = len(password)
    entropy = math.floor(math.log(r_total**l, 2))
    print(entropy)

    print("Very Weak"*(entropy < 28)+ \
        "Weak"*(28 <= entropy <= 35)+ \
        "Reasonable"*(36 <= entropy <= 59)+ \
        "Strong"*(60 <= entropy <= 127)+ \
        "Very Strong"*(entropy >= 128))
main()
