"Ticket Fare"
def lowest(x,y):
    "find lowest number"
    if x > y :
        return y
    return x

def main() :
    "main"
    last_station = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    start = int(input())
    stop = int(input())
    distance = abs(start-stop)
    total = 0

    #สถานีที่ไม่มี แสดงค่า Error
    if start <= 0 or stop <= 0 :
        print("Error")
        return
    if start > last_station or stop > last_station :
        print("Error")
        return

    # level 1
    if distance >= 0:
        total += b
        distance -= a
    # level 2
    if distance > 0 :
        total += d*(lowest(c,distance))
        distance -= c
    # level 3
    if distance > 0 :
        total += e*distance

    print(total)
main()
