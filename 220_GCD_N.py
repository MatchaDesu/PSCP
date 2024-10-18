"GCD_N"
def gcd(num1,num2) :
    "return gcd of pair"
    while num2 :
        num1, num2 = num2, num1 % num2
    return num1

def main() :
    "main"
    num = int(input())
    set_num = [int(input()) for _ in range(num)]
    curr_gcd = set_num[0]

    for i in set_num[1:] :
        curr_gcd = gcd(curr_gcd,i)

    print(curr_gcd)
main()
