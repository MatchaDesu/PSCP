"Sequence XI"
def main():
    "main"
    num = int(input())
    new_num = 2*num-1
    for col in range((-new_num)//2+1, new_num//2+1):
        for row in range((-new_num)//2+1, new_num//2+1):
            print(f"{(num-max(abs(col), abs(row))):02d}" ,end=" ")
        print()
main()
