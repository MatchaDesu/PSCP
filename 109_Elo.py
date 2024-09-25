"Elo"
def main(ra,rb,specific) :
    "main"
    ea = 1/(1+10**((rb-ra)/400))
    eb = 1/(1+10**((ra-rb)/400))
    print(f"{ea:.2f}"*bool(specific=="A")+f"{eb:.2f}"*bool(specific=="B"))
main(int(input()),int(input()),input())
