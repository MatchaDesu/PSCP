"Number Message"
def main() :
    "main"
    msg = str(input()).upper()

    msg = msg.replace("13","B")
    msg = msg.replace("12","R")
    msg = msg.replace("0","O")
    msg = msg.replace("5","S")
    msg = msg.replace("4","A")
    msg = msg.replace("3","E")
    msg = msg.replace("1","I")

    clear_num = ""
    for i in msg :
        if not i.isnumeric() :
            clear_num += i

    print(clear_num)
main()
