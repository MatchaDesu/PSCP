"ATM"
def main() :
    "main"
    money = int(input())
    while True :
        op = input()
        if op == "END" :
            break
        op = op.split()
        if op[0] == "D" :
            money += int(op[1])
        if op[0] == "W" :
            money = max(0,money-int(op[1]))
    print(money)
main()
