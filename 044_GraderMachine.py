""" GraderMachine """
def main():
    """ GraderMachine """
    x = int(input())
    y = int(input())
    z = 0
    print("pass : ",end="")
    if x > y :
        for i in range(x, y-1,-1):
            if not i%2 :
                print(i,end=" ")
                z += i
    else :
        for i in range(x, y+1,1):
            if not i%2 :
                print(i,end=" ")
                z += i
    print()
    print(f"Sum : {z}")
main()
