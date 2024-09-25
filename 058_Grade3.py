"Grade III"
import math
def grade(number) :
    "Grade"
    total = None
    if 95 <= number <= 100 :
        total = 4
    elif 90 <= number < 95 :
        total = 3.5
    elif 85 <= number < 90 :
        total = 3
    elif 80 <= number < 85 :
        total = 2.5
    elif 75 <= number < 80 :
        total = 2
    elif 70 <= number < 75 :
        total = 1.5
    elif 65 <= number < 70 :
        total = 1
    elif 60 <= number < 65 :
        total = 0.5
    elif 0 <= number < 60 :
        total = 0
    return total

def main() :
    "main"
    total = 0
    n = int(input())
    for _ in range(n):
        total += grade(float(input()))

    average = total/n
    average = math.floor(average*100)/100
    print(f"{average:.2f}")
main()
