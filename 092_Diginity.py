"Diginity"
def summation(num) :
    "summation the number into 1 digit"
    summ = num
    while len(str(num)) > 1 :
        summ = 0
        for i in str(num) :
            summ += int(i)
        num = summ
    return summ

def main() :
    "main"
    number = "Standby"
    while number :
        number = int(input())
        if number :
            print(summation(number))
main()
