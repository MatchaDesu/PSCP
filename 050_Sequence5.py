"Sequence V"
most = int(input())
COUNT = 0
for i in range(most,1-1,-1) :
    COUNT += 1
    if COUNT == 7 :
        print(i)
        COUNT = 0
    else :
        print(i,end=" ")
