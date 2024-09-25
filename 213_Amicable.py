"Amicable"
def check_factor(x) :
    "Check the number"
    sum_factor = 1

    for i in range(2, int(x**0.5)+1) :
        if not x % i :
            sum_factor += i
            if i != x // i :
                sum_factor += x // i

    return sum_factor

def main() :
    "main"
    stop = int(input())
    pair = []
    for i in range(2,stop) :
        num = check_factor(i)
        if num != i and i == check_factor(num) :
            pair.append(i)
    print(sum(pair))

main()
