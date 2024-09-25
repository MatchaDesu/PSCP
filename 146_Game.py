"Game"
def main(a,b) :
    "main"
    a_tie = a % 3
    b_tie = b % 3
    if a_tie == b_tie :
        print(a_tie)
    else :
        print("Error")
main(int(input()),int(input()))
