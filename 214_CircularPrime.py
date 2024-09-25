"CircularPrime"
def is_prime(x) :
    "Check the number"
    for i in range(2, int(x**0.5)+1) :
        if not x % i :
            return False
    return True

def main() :
    "main"
    total = 0
    stop = int(input())
    num = []

    for i in range(2,stop+1):
        num.append(i)
    for i in num :
        i = str(i)
        num_swap = [int(i[x:]+i[:x]) for x in range(len(i))]
        if all(map(is_prime,num_swap)) :
            total += int(i)
    print(total)

main()
