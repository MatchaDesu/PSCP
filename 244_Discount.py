"Discount"
def main() :
    "main"
    book_price = []
    n = 0

    while True :
        book = input()
        if book == "ENTER" :
            break
        book_price.append(int(book))

    book_price.sort()

    if 6 <= len(book_price) < 12 :
        n = 1
    elif 12 <= len(book_price) < 20 :
        n = 2
    elif 20 <= len(book_price) < 25 :
        n = 4
    elif len(book_price) >= 25 :
        n = 4 + (len(book_price)-20) // 5

    print(sum(book_price[n:]))
main()