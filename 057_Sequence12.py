"Sequence XII"
def main():
    "main"
    num = int(input())
    new_num = 2*num-1
    for row in range((-new_num)//2+1, new_num//2+1):
        for col in range((-new_num)//2+1, new_num//2+1):
            print(f"{(num-abs(abs(row) - abs(col))):02d}" ,end=" ")
        print()
main()
