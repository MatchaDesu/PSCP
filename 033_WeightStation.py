"Station"
def checking(w1,w2,w3,w4,avg):
    "Checking"
    last = w4
    x = sorted((w1,w2,w3,w4))
    for i in x :
        if abs(avg-i) > avg / 2 :
            print("Unbalance")
            return
    print(f"Pass {last:.2f}")
    return

def main():
    "main"
    avg = float(input())
    w1 = float(input())
    w2 = float(input())
    w3 = float(input())
    w4 = 4*avg - w1 - w2 - w3

    if w1 + w2 + w3 + w4 > 15000 :
        print("Overweight")
    else :
        checking(w1,w2,w3,w4,avg)
main()
