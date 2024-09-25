"GCD_v2"
def main() :
    "main"
    num1 = int(input())
    num2 = int(input())

    if min(num1, num2) <= 0 :
        print(max(num1,num2))
        return

    while num2 :
        num1, num2 = num2, num1 % num2

    print(num1)
main()
