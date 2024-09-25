"Rock Paper Scissor"
def match(a,b) :
    '''This function is for checking who is winning
    if a win return 1,0
    if b win return 0,1
    if ties return 0,0'''
    a_win = ("RS","SP","PR")
    b_win = ("SR","PS","RP")
    start = a + b
    if start in a_win :
        return 1, 0
    if start in b_win :
        return 0, 1
    return 0, 0

def main() :
    "main"
    fight = input()
    a = fight[0::2]
    b = fight[1::2]
    stop = len(a)
    counta, countb = 0, 0
    for i in range(stop) :
        counta += match(a[i],b[i])[0]
        countb += match(a[i],b[i])[1]

    if counta > countb :
        print(f"A win {counta}-{countb}")
    elif counta < countb :
        print(f"B win {countb}-{counta}")
    else :
        print(f"DRAW {counta}")
main()
