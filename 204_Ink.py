"Ink"
from math import ceil
def main() :
    "main"
    expand, people = list(map(int, input().split()))
    origin = 0

    for _ in range(people) :
        x, y = list(map(int, input().split()))
        distance = ((origin - x)**2 + (origin - y)**2)**0.5
        second = (3.1416*distance**2)/expand
        second = ceil(second)
        print(second)
main()
