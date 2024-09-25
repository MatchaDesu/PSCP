"One For All"
def main() :
    "main"
    gen = int(input())
    oneforall = ""
    for i in range(1,gen+1) :
        oneforall += input()
        if i != gen :
            if i % 2 :
                oneforall += "*"*i
            else :
                oneforall += "-"*i
        else :
            oneforall += f"_{gen}"
    print(oneforall)
main()
