"BloodDonation"
def main() :
    "main"
    age = int(input())
    weight = int(input())
    donated = int(input())

    if (not donated and age > 55) or weight < 45 or age < 17 or age > 70 :
        print("No")
        return

    if 17 < age < 60 :
        print("Yes")
        return

    if age == 17 :
        if input() == "True" :
            print("Yes")
            return

    if 60 <= age <= 70 :
        if input() == "True" :
            print("Yes")
            return

    print("No")

main()
