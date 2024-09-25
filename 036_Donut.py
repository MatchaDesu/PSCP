"Donut"
def main() :
    "main"
    price,buy,bonus,want = int(input()),int(input()),int(input()),int(input())
    pro_total = buy + bonus
    group = want // pro_total
    if not want :
        print("0 0")
    else :
        donut = pro_total * group
        remain = want - donut
        if remain > buy :
            remain = buy
        if remain >= buy :
            donut += pro_total
        else :
            donut += remain
        print(f"{price * group * buy + (remain*price)} {donut}")
main()
