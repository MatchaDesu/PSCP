"FibonacciRecursionV1"
def main(n):
    "main"
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return main(n - 1) + main(n - 2)
print(main(int(input())))
