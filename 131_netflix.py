"Netflix"
def main() :
    "main"
    screen = int(input())
    number_phone = int(input())

    device = input()
    device = input() #Don't care

    device = input()
    hd = input()
    ultra = input()
    premium = 0
    standard = 0
    basic = 0
    mobile = 0
    total = 0

    while screen > 0 or number_phone > 0 :
        if (screen >= 3 or number_phone >= 3) and \
            (device == "Yes" or hd == "Yes" or ultra == "Yes") :
            premium += 1
            total += 419
            screen -= 4
            number_phone -= 4

        elif (screen >= 2 or number_phone >= 2) and \
            (device == "Yes" or hd == "Yes") :
            standard += 1
            total += 349
            screen -= 2
            number_phone -= 2

        elif device == "Yes" and hd == "No" and ultra == "No" :
            basic += 1
            total += 279
            screen -= 1
            number_phone -= 1

        else :
            if ultra == "Yes" :
                premium += 1
                total += 419
                screen -= 4
                number_phone -= 4

            elif hd == "Yes" :
                standard += 1
                total += 349
                screen -= 2
                number_phone -= 2

            elif device == "Yes" :
                basic += 1
                total += 279
                screen -= 1
                number_phone -= 1

            else :
                mobile += 1
                total += 99
                screen -= 1
                number_phone -= 1

    package(premium,standard,basic,mobile,total) #เรียกใช้ฟังก์ชั่นให้ print output ออกมา

def package(premium,standard,basic,mobile,total) :
    "Print Output"
    print(( f"Premium x {premium}\n"*bool(premium) + \
    f"Standard x {standard}\n"*bool(standard) + \
    f"Basic x {basic}\n"*bool(basic) + \
    f"Mobile x {mobile}\n"*bool(mobile) ).strip())
    print("Total =",total,"THB")

main()
        