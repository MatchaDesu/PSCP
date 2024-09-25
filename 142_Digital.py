"Digital"
def main() :
    "main"
    name = input()
    national = bool(str(input()) in ("Yes","True"))
    house = bool(str(input()) in ("Yes","True"))
    age = bool(float(input())>= 16)
    income = bool(float(input())<=840000)
    money = bool(float(input())<=500000)
    if national and house and age and income and money :
        print(f"Congratulations! {name} is qualified \
to receive a digital wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else :
        print(f"Unfortunately, {name} is not qualified.")
main()
