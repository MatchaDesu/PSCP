"Lift"
def main() :
    "main"
    people = int(input())
    weight_limit = float(input())
    weight_total = 0
    kid = True
    if not people :
        print("Safe")
        return
    for _ in range(people) :
        age = int(input())
        weight = float(input())
        if age >= 12 :
            kid = False
        weight_total += weight
    if not kid and weight_total <= weight_limit :
        print("Safe")
    else :
        print("Not Safe")
main()
