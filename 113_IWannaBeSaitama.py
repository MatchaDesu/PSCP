"I want to be Saitama"
from math import ceil
def most(x,y) :
    "Return the most number"
    if x >= y :
        return x
    return y

def main() :
    "main"
    most_day = 0
    task1 = int(input())
    task2 = int(input())
    task3 = int(input())
    task4 = int(input())
    most_day = 0
    most_day = most(most_day,ceil(task1/int(input())))
    most_day = most(most_day,ceil(task2/int(input())))
    most_day = most(most_day,ceil(task4/int(input())))
    most_day = most(most_day,ceil(task3/int(input())))
    print(most_day)
main()
