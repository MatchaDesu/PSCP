"Bus Seat"
def main() :
    "main"
    row = int(input())
    seats = int(input())
    myseat = int(input())
    current_row = []
    bus = []
    index = 1
    step = 0
    count = 0

    for _ in range(row) :
        for _ in range(seats) :
            if index+step == myseat :
                current_row.append("XX")
            else :
                current_row.append(f"{index+step:02}")
            step += row

        bus.append(current_row)
        current_row = []
        index += 1
        step = 0

    for i in bus[::-1] :
        if not count % 2 and count :
            print()
        print(" ".join(i))
        count += 1
main()
