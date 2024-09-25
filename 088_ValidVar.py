"Valid Var"
restrict = ("if","else","elif","while","for","True","False","continue","break", \
    "return","is","in","and","or","from","as","pass","not","def","None")

def main() :
    "main"
    num = int(input())
    for _ in range(num) :
        var_name = input()
        var_name = var_name.strip()
        if var_name.isidentifier() :
            if var_name in restrict :
                print("Invalid")
            else :
                print("Valid")
        else :
            print("Invalid")
main()
