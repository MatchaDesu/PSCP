"MultiplyMatrixPQR"
def main() :
    "main"
    m = int(input())
    n = int(input())
    p = int(input())
    matrix_a, matrix_b = [], []
    mutiplicated = []
    total = 0
    count = 0

    for _ in range(m) :
        a = []
        for _ in range(n) :
            a.append(int(input()))
        matrix_a.append(a)

    for _ in range(n) :
        b = []
        for _ in range(p) :
            b.append(int(input()))
        matrix_b.append(b)

    #print(*matrix_a,sep="\n")
    #print(*matrix_b,sep="\n")

    for i in range(m) :
        for j in range(p) :
            for k in range(n) :
                total += matrix_a[i][k] * matrix_b[k][j]
            mutiplicated.append(total)
            total = 0

    for i in range(m*p) :
        count += 1
        print(mutiplicated[i],end=" ")

        if count == p :
            count = 0
            print()
main()
