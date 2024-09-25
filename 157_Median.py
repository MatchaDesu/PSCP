"Median"
import statistics
def main() :
    "main"
    num = []
    for _ in range(int(input())) :
        num.append(float(input()))
    print(f"{statistics.median(num):.3f}")
main()
