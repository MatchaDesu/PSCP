"DNA"
def main() :
    "main"
    dna_type = ("A","C","G","T")
    fisrt_dna = input()
    second_dna = input()
    discovered = ""
    longest = ""

    if len(second_dna) > len(fisrt_dna) :
        fisrt_dna,second_dna = second_dna,fisrt_dna

    for i in second_dna :
        if i not in dna_type :
            print("Error")
            return

    for i in fisrt_dna :
        discovered += i

        if i not in dna_type :
            print("Error")
            return

        if discovered not in second_dna :
            for _ in range(len(discovered)) :
                if len(discovered) > 0 :
                    discovered = discovered[1:]
                    if discovered in second_dna :
                        break

        if discovered in second_dna :
            if len(discovered) > len(longest) :
                longest = discovered

    if longest :
        print(longest)
        return
    print("None")

main()
