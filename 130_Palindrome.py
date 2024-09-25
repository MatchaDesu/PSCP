"Palindrome"
def main() :
    "main"
    end   = int(input())
    time  = input()
    count = 0

    while count < end :
        mi_nute = f"{int(time[-2:]) + 1:>02}"
        hour = time[0:2].replace(":", "")
        if not int(mi_nute) % 60 and int(mi_nute):
            mi_nute = "00"
            hour = str(int(hour)+1)
        if not int(hour) % 24:
            hour = "0"
        time = hour + ":" + mi_nute
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            count += 1
            print(time)

main()
