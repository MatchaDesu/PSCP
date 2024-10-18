"T-score"
def main() :
    "main"
    n = int(input())
    _ = int(input())
    all_people = []

    for _ in range(n) :
        all_people.append(int(input()))

    x_bar = sum(all_people)
    x_bar2 = sum(map(lambda x : x**2, all_people))

    sd = (((n*x_bar2) - (x_bar**2))/(n*(n-1)))**0.5

    z = list(map(lambda x :(x - x_bar/n)/sd, all_people))

    for i in z :
        print(f"{50+10*i:.2f}")

main()
