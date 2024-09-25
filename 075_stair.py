"Stair"
def main():
    "main"
    reached = int(input())
    total_steps = int(input())
    current = 0
    count = 0
    for _ in range(total_steps):
        height = int(input())
        if height > reached:
            print("NO")
            return
        current += height
        if current >= reached:
            count += 1
            if current == reached:
                current = 0
            elif current > reached:
                current -= current - height
        if current > reached:
            print("NO")

    if current > 0:
        count += 1
    if not reached:
        count = 0
    print(count)

main()
