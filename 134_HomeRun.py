"Home Run"
def main() :
    "main"
    number = int(input())
    how_far = float(input())
    count = 0
    for _ in range(number) :
        if how_far > float(input()) :
            count +=1
    print(count)
main()
