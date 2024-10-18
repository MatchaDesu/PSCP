"RunGame"
def main() :
    "main"
    distancce = 0
    runway = [0] + input().split()
    for i in range(1,len(runway)) :
        distancce += abs(int(runway[i]) - int(runway[i-1]))
    print(distancce)
main()
