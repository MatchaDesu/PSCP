"Nearrer"
def main():
    "main"
    alice,bob,car = int(input()),int(input()),int(input())
    d_a = abs(car-alice)
    d_b = abs(car-bob)
    if d_a > d_b :
        print(f"Bob {d_b}")
    elif d_a < d_b:
        print(f"Alice {d_a}")
    else :
        print(f"Sundaes {d_a}")
main()
