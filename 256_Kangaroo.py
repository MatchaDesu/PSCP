"Kangaroo"
def main() :
    "main"
    kangaroo = []
    count = 0

    for _ in range(3) :
        kangaroo.append(int(input()))

    first,second,third = kangaroo[0],kangaroo[1],kangaroo[2]

    while True :
        distance1 = second - first
        distance2 = third - second

        #print(first,second,third)
        if distance1 < 2 and distance2 < 2 :
            break
        if distance2 > 1 :
            first,second = second,third - 1
        elif distance1 > 1 :
            third,second = second,first + 1
        count += 1

    print(count)
main()
