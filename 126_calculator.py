"Calculator"
def main() :
    "main"
    num = int(input())
    button = ""
    if num > 1 :
        for i in range(1,num+1) :
            button += f"{i}"+"+"*(not i==num)+(i==num)*"="
        print(len(button))
    else :
        print(1)
main()
