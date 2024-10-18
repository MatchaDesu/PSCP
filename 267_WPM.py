"WPM"
def kid(wpm) :
    "kid type"
    if wpm < 11 :
        return "Very Slow"
    if 11 <= wpm <= 20 :
        return "Slow"
    if 20 < wpm <= 30 :
        return "Average"
    if 30 < wpm <= 40 :
        return "Fast"
    return "Very Fast"

def adult(wpm) :
    "adult type"
    if wpm < 26 :
        return "Very Slow"
    if 26 <= wpm <= 35 :
        return "Slow/Beginner"
    if 35 < wpm <= 45 :
        return "Intermediate/Average"
    if 45 < wpm <= 65 :
        return "Fast/Advanced"
    if 65 < wpm <= 80 :
        return "Very Fast"
    return "Insane"

def main() :
    "main"
    age = input()
    wpm = int(input())
    if age == "Kids" :
        print(kid(wpm))
    else :
        print(adult(wpm))
main()
