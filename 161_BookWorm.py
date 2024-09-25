"Book Worm"
def main() :
    "main"
    book = []
    total_time = 0
    count = 0
    for _ in range(int(input())) :
        time = float(input())

        for i in range(int(input())) :
            book.append(float(input()))
        book.sort()

        for i in book :
            total_time += i
            if total_time <= time :
                count += 1

        print(count)
        count,total_time = 0, 0
        book.clear()

main()
