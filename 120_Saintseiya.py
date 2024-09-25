"Saint Seiya"
def main() :
    "main"
    punch = 0
    second = int(input())
    limit = int(input())
    time_left = 0

    for i in range(2,second+1,2) :
        if punch >= limit :
            time_left = second - i + 1
            break
        if not i % 6 :
            punch += 1
        elif not i % 2 :
            punch += 165

    punch += (time_left)*12
    print(punch)
main()
