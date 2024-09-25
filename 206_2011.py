"2011"
def main() :
    "main"
    week = {
        1 : 'Saturday',
        2 : 'Sunday',
        3 : 'Monday',
        4 : 'Tuesday',
        5 : 'Wednesday',
        6 : 'Thursday',
        0 : 'Friday'
    }

    day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = int(input())
    month = int(input())
    total_day = 0

    for i in range(1,month) :
        total_day += day_in_month[i-1]
    total_day += day

    print(week[total_day%7])
main()
