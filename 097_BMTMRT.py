"""BTSMRT"""
def main():
    """BTSMRT"""
    holiday,age,tall = input(),float(input()),float(input())

    if holiday == "Children Day":
        if age < 14 and tall <= 140:
            print("FREE")
        else:
            print("PAY")

    if holiday == "Senior Day":
        if age >= 60:
            print("FREE")
        elif age < 14 and tall < 90:
            print("FREE")
        else:
            print("PAY")

    if holiday == "Normal Day":
        if age < 14 and tall <= 90:
            print("FREE")
        else:
            print("PAY")
main()
