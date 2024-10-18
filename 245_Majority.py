"Majority"
def main() :
    "main"
    major = list(range(1,int(input())+1))
    people = int(input())

    major_dict = dict.fromkeys(major,0)

    for _ in range(people) :
        major_dict[int(input())] += 1

    most = sorted(major_dict.items(), key=lambda x : x[1] )
    most = list(filter(lambda x : x[1] > people // 2, most))

    if most :
        print(*most[-1])
    else :
        print(0, max(major_dict.values()))
main()
