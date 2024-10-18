"PrasomSib"
def main() :
    "main"
    num = [int(i) for i in input()]
    counted = []
    text = []
    count = 0

    for i in range(len(num)-1) :
        text.append(num[i])

        for j in range(i+1,len(num)) :
            text.append(num[j])

            if sum(text) > 10 :
                break
            if sum(text) == 10 :
                counted.append(text)
                count += 1
                break

        text = []

    print(count)
main()
