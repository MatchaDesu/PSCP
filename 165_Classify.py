"Classify"
def gen(id_num) :
    "Return generation and facility id of student"
    return int(id_num[0]),int(id_num[1])

def main() :
    "main"
    id_studend = []
    checked = []
    year = []

    while True :
        data = str(input())
        if data in "END" :
            break
        id_studend.append([data[:2],data[2:4]])

    id_studend.sort(key=gen)

    for i in id_studend :
        if i not in checked :

            if i[0] not in year:
                year.append(i[0])
                checked.append(i)
                print(i[0],int(i[1]),id_studend.count(i))

            else :
                checked.append(i)
                print("--",int(i[1]),id_studend.count(i))
main()
