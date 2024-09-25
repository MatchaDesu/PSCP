"Lotto"
def main() :
    "main"
    jackpot = str(input())
    back_two = str(input())
    front_three_1, front_three_2 = str(input()), str(input())
    back_three_1, back_three_2 = str(input()), str(input())
    buy = str(input())
    reward = 0

    close_jackpot_up = str(int(jackpot) + 1)
    close_jackpot_down = str(int(jackpot) - 1)

    if int(close_jackpot_up) > 999999 :
        close_jackpot_up = "000000"
    if int(close_jackpot_down) < 0 :
        close_jackpot_down = "999999"

    close_jackpot_up = f"{close_jackpot_up:>06}"
    close_jackpot_down = f"{close_jackpot_down:>06}"

    reward += (front_three_1,front_three_2).count(buy[:3])*4000

    reward += (back_three_1,back_three_2).count(buy[-3:])*4000

    if buy[-2:] in back_two :
        reward += 2000

    if buy in (close_jackpot_down,close_jackpot_up) :
        reward += 100000

    if buy in jackpot :
        reward += 6000000
    print(reward)
main()
