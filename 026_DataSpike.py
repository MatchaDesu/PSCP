"DataSpike"
def most(num,current) :
    "Ordering"
    if num >= current :
        current = num
    return current

def main():
    "main"
    current = int(input())
    current = most(int(input()),current)
    current = most(int(input()),current)
    current = most(int(input()),current)
    current = most(int(input()),current)
    current = most(int(input()),current)
    current = most(int(input()),current)
    current = most(int(input()),current)
    print(current)
main()
