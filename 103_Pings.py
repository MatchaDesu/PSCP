"Pings"
from math import floor
def directory(line) :
    "find ip from directory line"
    index_start = line.find("Pinging") + 8
    index_end = line.find(" with")
    ping = line[index_start:index_end]
    return ping

def pinging(line) :
    "find ip from Pinging line"
    index_start = line.find("[") + 1
    index_end = line.find("]")
    ping = line[index_start:index_end]
    return ping

def time_received(line) :
    """Return Time,Succesful
    Ex. 24ms,1(0 if loss)"""
    if "time=" in line :
        time_start = line.find("time=") + 5
        time_end = line.find("ms")
        time = line[time_start:time_end]
        return time,1
    if "time<1ms" in line :
        return "0",1
    return None,None

def main():
    "main"
    location = ""
    recieve = 0
    lost = 0
    trip_time_max,trip_time_min = 0,1000000000000000000000000000000
    total = 0
    ip = ""
    location = input()
    location = input()
    location = input()
    if location.find("[") != -1 :
        ip = pinging(location)
    else :
        ip = directory(location)

    for _ in range(4) :
        trip_time,succesful = time_received(input())
        if succesful :
            trip_time = int(trip_time)
            recieve += 1
            trip_time_max = max(trip_time_max,trip_time)
            trip_time_min = min(trip_time_min,trip_time)
            total += trip_time
        else :
            lost += 1
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {recieve}, Lost = {lost} ({lost*25}% loss),")
    if recieve :
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {trip_time_min}ms, Maximum = {trip_time_max}ms, Average" \
            f" = {floor(total/recieve)}ms")
main()
