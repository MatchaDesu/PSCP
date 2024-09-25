"Tuple's Sad life"
def main() :
    "main"
    text = input().split()
    number = input()
    count = text.count(number)
    index = text.index(number)
    counting = 0
    for _ in range(1,count**2+1) :
        counting += 1
        if counting != count :
            print(index,end=" ")
        else :
            counting = 0
            print(index)
main()
