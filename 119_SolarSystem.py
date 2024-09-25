"Solar System"
def main() :
    "main"
    solar = " " + input() + " "
    solar = solar.replace(" Sun ","0") #เปลี่ยนคำว่า " Sun " เป็น 0 เพื่อง่ายต่อการ Slicing

    left_planet = solar[:solar.find("0")].strip() #Slicing ดาวเคราห์ทางซ้าย
    right_planet = solar[solar.find("0")+1:].strip() #Slicing ดาวเคราห์ทางขวา

    left_total = left_planet.count(" ") #ถ้าเป็น 0 คือ มี 0-1 ดวง ("","Mars")
    right_total = right_planet.count(" ") #ถ้าเป็น 0 คือ มี 0-1 ดวง ("","Mars")

    left_hot, left_cool = "", ""
    right_hot, right_cool = "", ""

    if left_planet : #ถ้าทางซ้ายมีดาวเคราะห์ ถ้าไม่มี left_planet จะเป็น ""
        if not left_total : #มีดาวเคราะห์ดวงเดียว เช่น "Mars" ไม่มี space จะได้ออกมาเป็น 0
            left_hot = left_planet
            left_cool = left_planet
        else : #มี 1 ดวงขึ้นไป เช่น "Mars Earth" จะมี space คั่นในแต่ละดวง
            left_hot = left_planet[-1:left_planet.rfind(" "):-1][::-1]
            left_cool = left_planet[:left_planet.find(" ")]

    if right_planet : #ถ้าทางขวามีดาวเคราะห์ ถ้าไม่มี right_planet จะเป็น ""
        if not right_total : #มีดาวเคราะห์ดวงเดียว เช่น "Mars" ไม่มี space จะได้ออกมาเป็น 0
            right_hot = right_planet
            right_cool = right_planet
        else : #มี 1 ดวงขึ้นไป เช่น "Mars Earth" จะมี space คั่นในแต่ละดวง
            right_hot = right_planet[:right_planet.find(" ")]
            right_cool = right_planet[-1:right_planet.rfind(" "):-1][::-1]

    print("Hot: " + ( left_hot*(bool(left_planet)) + " " + right_hot*(bool(right_planet))).strip())
    print("Cool: " + ( left_cool*(bool(left_planet) and left_total >= right_total ) + " " \
                + right_cool*(bool(right_planet) and left_total <= right_total)).strip())

main()
