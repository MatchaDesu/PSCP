"Parallelogram"
def main() :
    "main"
    word = input()
    for i in range(1,len(word)+1) :
        print(f"{word[0:i]:>{len(word)}}")

    for i in range(1,len(word)) :
        print(f"{word[i:]}")
main()
