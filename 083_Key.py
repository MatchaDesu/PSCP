"Key"
def main() :
    "main"
    msg = str(input())
    sum_ = 0
    for i in msg :
        sum_ += int(i)
    product = int(msg[-3:])*10

    total = sum_ + product

    if total < 1000 :
        total += 1000

    print(str(total)[-4:])
main()
