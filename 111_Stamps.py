"Stamps"
from math import ceil
def main() :
    "main"
    visit = int(input())
    pro = int(input()) #a
    stamp_get = int(input()) #b
    stamp_use = int(input()) #c ( Use per times )
    discount = int(input()) #d
    payment = 0
    total_stamp = 0
    if stamp_get and discount :
        for _ in range(visit) :
            bill = int(input())
            if total_stamp < stamp_use :
                payment += bill
                total_stamp += (bill // pro)*stamp_get
            else :
                use_per_time = min(total_stamp//stamp_use,ceil(bill/discount))
                payment += max(0,bill - discount*use_per_time)
                total_stamp += (max(0,bill - discount*use_per_time)//pro)*stamp_get
                total_stamp -= stamp_use*use_per_time
    else :
        for _ in range(visit) :
            payment += int(input())
    print(payment)
    print(total_stamp)
main()
