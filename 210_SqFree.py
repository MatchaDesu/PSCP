"SqFree"
def main() :
    "main"
    num = int(input())
    count = 0

    for i in range(1,num+1) :
        if i > 3 :
            for j in range(2,int(i**0.5)+1) :
                if not i % j**2 :
                    break
                if j == int(i**0.5) :
                    count += 1
        else :
            count += 1
    print(count)
main()
