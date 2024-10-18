"GasStations"
def furthest(pos,r,d_list) :
    "return the most distance that can reach"
    d_list = list(filter(lambda x : pos <= x <= pos+r, d_list))
    return d_list

def main() :
    "main"
    c = float(input())
    r = float(input())
    pumps = int(input())
    road = []
    pos, station = 0, 0
    count = 0

    road.append(0)

    for _ in range(pumps) :
        station = float(input())
        if 0 < station < c and station not in road :
            road.append(station)

    road.sort()
    road.append(c)

    while True :
        pos = furthest(pos,r,road)[-1]

        if c == pos :
            break

        if len(furthest(pos,r,road)) <= 1 :
            print("depleted")
            return


        count += 1

    print(count)

main()
