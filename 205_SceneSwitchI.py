"SceneSwitch I"
def main() :
    "main"
    time = 0
    click = 0
    count = 0
    state = "on"
    color = "cool"
    cooldown = True

    while True :
        switch = input()
        if switch in "End" :
            break
        switch = float(switch)
        click += 1

        if state == "off" and color == "cool" and switch - time <= 6 and cooldown:
            color = "warm"
            cooldown = False
            count += 1
        elif state == "on" and color == "warm" and not cooldown:
            cooldown = True
        else :
            color = "cool"

        if not click % 2 :
            state = "off"
        else :
            state = "on"

        time = switch
        #print(click,state,color)
    print(count)
main()
