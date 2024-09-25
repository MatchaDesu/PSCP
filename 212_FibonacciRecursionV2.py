"FibonacciRecursionV2"
def main(n, memo=None):
    "main"
    if memo is None:
        memo = {0:0,1:1}
    if n in memo:
        return memo[n]
    if n >= 100 :
        main(n - 100, memo)
    memo[n] = main(n-1, memo) + main(n-2, memo)
    return memo[n]

print(main(int(input())))
