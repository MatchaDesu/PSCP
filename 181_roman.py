"Roman"
def main() :
    "main"
    roman = {
        'I'  : 1,
        'IV' : 4,
        'V'  : 5,
        'IX' : 9,
        'X'  : 10,
        'XL' : 40,
        'L'  : 50,
        'XC' : 90,
        'C'  : 100,
        'CD' : 400,
        'D'  : 500,
        'CM' : 900,
        'M'  : 1000
    }

    i = 0
    num = input()
    total = 0
    while i < len(num) :
        if num[i:i+2] in roman and i+1 < len(num) :
            total += roman[num[i:i+2]]
            i += 2
        else :
            total += roman[num[i]]
            i += 1
    print(total)

main()
