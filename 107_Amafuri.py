"Amafuri"
def day(weather) :
    "drying day time"
    if weather == "C" :
        return 0.5
    if weather == "N" :
        return 1
    return 1.5

def night(weather) :
    "drying night time"
    if weather == "C" :
        return 0.25
    if weather == "N" :
        return 0.5
    return 0.75

def rain(weather) :
    "rain"
    if weather == "R" :
        return 2
    return 3

def main() :
    "main"
    hour = int(input())
    weather = input()
    wet_guage = 8
    lost = 0
    dry = 0
    for i in weather.upper() :

        if i in ("C","N","W") :
            if 6 <= hour < 18 :
                wet_guage -= day(i)
            else :
                wet_guage -= night(i)

        if i in ("R","S") :
            wet_guage += rain(i)

        if i == "H" :
            lost = 1
            break

        if wet_guage <= 0 :
            dry = 1
            break

        if wet_guage > 16 :
            wet_guage = 16

        hour += 1

        if hour > 24 :
            hour -= 24

    if dry :
        print("Dry")
    elif lost :
        print("Lost")
    else :
        print(f"Still Wet (Wet Level: {wet_guage:.2f})")
main()
