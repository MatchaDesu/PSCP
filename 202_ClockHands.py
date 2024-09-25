"ClockHands"

def main() :
    "main"
    hour = int(input())
    minute = int(input())
    degree_hour = (hour*60 + minute)/2
    degree_minute = minute*6

    if degree_hour - degree_minute > 6 or degree_hour < degree_minute:
        print(False)
    else :
        print(True)

main()
