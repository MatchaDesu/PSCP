"B - Fully pair?"
def main() :
    "main"
    letter = input()
    no_pair = ""

    for i in letter :
        if letter.count(i) % 2 and i not in no_pair:
            no_pair += i
    print(f"{no_pair}"*(len(no_pair)>0)+"fully paired"*(not len(no_pair)>0))
main()
