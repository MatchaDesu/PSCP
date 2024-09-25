"Meteorite"
def main() :
    "main"
    a = float(input())
    b = int(input())
    c = float(input())
    missile = 0
    state = 0
    while a >= c :
        missile += b**state
        state += 1
        a /= b
    print(missile)
main()
