"Backward"
def main() :
    "main"
    text = None
    text_list = []
    while True :
        text = str(input())

        if text in "NULL" :
            break

        text_list.append(text)

    text_list.reverse()
    for i in text_list :
        print(i)
main()
