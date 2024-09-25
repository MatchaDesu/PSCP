"kapreka"
def ordering(list_of_number) :
    "Turn list of number into low to high list"
    lenght = len(list_of_number)
    ls = []
    for i in list_of_number :
        ls += i
    for i in range(lenght) :
        for j in range(i+1,lenght) :
            if ls[i] >= ls[j] :
                ls[i],ls[j] = ls[j],ls[i]
    return ls

def main() :
    "main"
    number = int(input())
    bigger = ""
    smaller = ""
    count = 0
    while number != 6174 :
        count += 1
        low_to_high = ordering(str(number))
        high_to_low = low_to_high[::-1]
        for i in high_to_low :
            bigger += i
        for i in low_to_high :
            smaller += i
        number = int(f"{bigger:<04}") - int(smaller)
        bigger = ""
        smaller = ""
    print(count)
main()
