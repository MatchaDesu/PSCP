"ScaledMatrix"
def main() :
    "main"
    m = int(input())
    n = int(input())
    matrix = []
    count = 0

    for _ in range(m*n) :
        matrix.append(float(input()))

    for i in matrix :
        count += 1
        print(f"{(i-min(matrix))/(max(matrix)-min(matrix)):.2f}",end=" ")
        if count == n :
            count = 0
            print()
main()
