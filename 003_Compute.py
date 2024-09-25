"Compute"
def main() :
    "main"
    milsec = 492137954293754252786
    sec = milsec // 1000
    milsec = milsec % 1000
    minutes = sec // 60
    sec = sec % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours  =hours % 24
    print(days,hours,minutes,sec,milsec)
main()
