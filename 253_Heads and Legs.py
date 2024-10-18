"Heads and Legs"
def main() :
    "main"
    total_head = int(input())
    total_leg = int(input())
    rabbit = (total_leg - 2*total_head)/2
    bird = total_head - rabbit

    if (rabbit >= 0 and bird >= 0) and not ( rabbit % 1 or bird % 1):
        print(int(rabbit),int(bird))
    else :
        print("Impossible")
main()
