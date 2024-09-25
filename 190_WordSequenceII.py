"WordSequence II"
def main() :
    "main"
    text1 = list(input())
    text2 = list(input())
    min_len = min(len(text1),len(text2))
    i = 0

    print("".join(text1))
    while i < min_len :
        if text1 != text2 :
            text1[i] = text2[i]
        i += 1
        print("".join(text1))

    if len(text1) > len(text2) :
        while text1 != text2 :
            text1.pop(i)
            print("".join(text1))

    elif len(text1) < len(text2) :
        while text1 != text2 :
            text1.append(text2[i])
            i += 1
            print("".join(text1))

main()
