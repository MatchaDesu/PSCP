"Harshad"
def summation(num) :
    """นำเลขโดดมาบวกกัน
    เช่น 543 > 5+4+3
    return 12"""
    total = 0
    for i in str(abs(num)) :
        total += int(i)
    return total

def main():
    "main"
    for _ in range(10) :
        num = int(input())
        if num :
            if not num % (summation(num)) :
                print("Yes")
            else :
                print("No")
        else :
            print("No")
main()
