"IP Address"
def main() :
    "main"
    ip = input().split(".")
    real_ip = []

    if len(ip) != 4 :
        print("Invalid IPv4 address")
        return

    for i in ip :
        for j in i :
            if not j.isnumeric() :
                print("Invalid IPv4 address")
                return

        if int(i) > 255 or int(i) < 0 :
            print("Invalid IPv4 address")
            return

        real_ip.append(str(int(i)))
    print(".".join(real_ip))
main()
