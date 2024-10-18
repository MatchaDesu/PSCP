"OTP"
from collections import Counter
def main() :
    "main"
    while True :
        otp = str(input())
        if otp == "0" :
            break

        number_feq = list(Counter(otp).values())

        if len(otp) == 4 :
            if number_feq.count(2) == 1 :
                print("Valid")
                continue

        elif len(otp) == 6 :
            if number_feq.count(2) == 2 or number_feq.count(3) == 1:
                print("Valid")
                continue

        elif len(otp) == 8 :
            if number_feq.count(2) == 3 or number_feq.count(3) == 2 :
                print("Valid")
                continue

        print("Invalid")
main()
