"""Sequence X"""
def main(num):
    """Sequence X"""
    for i in range(1 ,num+1):
        for j in range(num - i):
            print("  ", end = " ")
        for j in range(1, i):
            print(f"{j:02}", end = " ")
        for i in range(i, 0, -1):
            print(f"{i:02}" , end = " ")
        print()
    for i in range(num-1, 0, -1):
        for j in range(0, num - i):
            print("  ", end = " ")
        for j in range(1, i):
            print(f"{j:02}", end = " ")
        for i in range(i, 0, -1):
            print(f"{i:02}" , end = " ")
        print()
main(int(input()))
