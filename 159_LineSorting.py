"Line Sorting"
def main() :
    "main"
    text = []
    for _ in range(int(input())) :
        text.append(str(input()))
    text.sort(key=len)
    for i in text :
        print(i)
main()
