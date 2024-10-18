"Semi Prime"
def all_prime(x) :
    "find that number is prime or not"
    if x <= 1 :
        return False

    for i in range(2, int((x)**0.5)+1) :
        if not x % i :
            return False
    return True


def main() :
    "main"
    num = int(input())
    primes = list(filter(all_prime, list(range(num))))
    counted = []
    total = 0

    for i in primes :
        for j in primes :
            if i*j <= num and (i,j) not in counted:
                total += 1
            elif i*j > num :
                break
            counted.append((j,i))

    print(total)
main()
