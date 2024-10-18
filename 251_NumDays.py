"NumDays"
def main() :
    "main"
    day_start = int(input())
    month_start = int(input())
    day_end = int(input())
    month_end = int(input())
    total_day_start = 0
    total_day_end = 0

    year = [31,28,31,30,31,30,31,31,30,31,30,31]

    if day_start > year[month_start-1] or day_end > year[month_end-1] :
        print("Impossible")
        return

    for i in range(month_start) :
        if i + 1 == month_start :
            total_day_start += day_start
            break
        total_day_start += year[i]

    for i in range(month_end) :
        if i + 1 == month_end :
            total_day_end += day_end
            break
        total_day_end += year[i]

    #print(total_day_start)
    #print(total_day_end)
    print(abs(total_day_start-total_day_end))
main()
