"Filter"
import json

def main() :
    "main"
    score = json.loads(input())
    threshold = float(input())
    score = dict(filter(lambda x : x[1] >= threshold,\
        sorted(score.items(),key=lambda x : int(x[0]))))

    if score:
        for i,j in score.items() :
            print(i,f"{j:.2f}",sep="\t")
    else :
        print("Nope")

main()
