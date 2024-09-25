"Almost Mean"
def main() :
    "main"
    n = int(input())
    studend, score = [], []
    most = 0
    most_score = 0

    for i in range(n) :
        id_num, score_num = input().split()
        studend.append(id_num)
        score.append(float(score_num))

    average = sum(score)/n

    for i in range(n) :
        if score[i] <= average and score[i] > most_score :
            most = i
            most_score = score[i]

    print(f"{studend[most]}\t{score[most]}")
main()
