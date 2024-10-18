"Pad Thai"
def main() :
    "main"
    ingrediant = {
        "Pad Thai Sauce" : "excluded",
        "Tofu" : "excluded",
        "Pickle Turnip" : "excluded",
        "Shrimp" : "excluded",
        "Bean Sprouts" : "excluded",
        "Noodle" : "excluded",
        "Chives" : "excluded",
        "Lime" : "excluded",
        "Egg" : "excluded",
        "Oil" : "excluded",
        "Peanuts" : "excluded"
    }

    ingre_list = list(ingrediant.keys())

    taste = {
        "Sweet" : "excluded",
        "Sour" : "excluded",
        "Salty" : "excluded"
    }

    taste_list = list(taste.keys())

    while True :
        cook = input()
        if cook == "Cook" :
            break
        if cook in ingre_list :
            ingrediant[cook] = "included"
        else :
            ingrediant[cook] = "do not need"

    while True :
        cook = input()
        if cook == "End" :
            break
        if cook in taste_list :
            taste[cook] = "included"
        else :
            taste[cook] = "excluded"

    if "do not need" in ingrediant.values() :
        print("This is not Pad Thai!!!")
        return

    if "excluded" in ingrediant.values() :
        print("This is bad!")
        return

    if "excluded" in taste.values() :
        print("Not Bad...")
        return

    #ผ่านทุกเงื่อนไข
    print("Delicious!")
main()
