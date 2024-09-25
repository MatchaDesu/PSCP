"IT Business"
def main() :
    "main"
    in_bank = float(input())
    in_hand = float(input())
    action = "stanby"
    error = 0
    while action != "end" and error < 3 :
        action = input()
        if action != "end" :
            if action[:1] in "D" :
                if in_hand >= float(action[2:]) :
                    in_hand -= float(action[2:])
                    in_bank += float(action[2:])
                    error = 0
                else :
                    error += 1
            elif action[:1] in "W" :
                if in_bank >= float(action[2:]) :
                    in_hand += float(action[2:])
                    in_bank -= float(action[2:])
                    error = 0
                else :
                    error += 1
            else :
                error += 1
    print(f"{in_bank:.2f}")
    print(f"{in_hand:.2f}")
main()
