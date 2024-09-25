"Turnstile"
def main() :
    "main"
    action = "Standby"
    state = "Locked"
    count = 0
    while action != "END" :
        action = input()
        if action != "End" :
            if state == "Unlocked" and action == "P" :
                count += 1
            if action == "C" :
                state = "Unlocked"
            if action == "P" :
                state = "Locked"
    print(count)
main()
