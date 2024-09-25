"""BigFrame"""
def main():
    "main"
    msg_group = str(input()),str(input()),str(input()),str(input()),str(input())
    maxx = 0
    for i in msg_group :
        if maxx <= len(i.strip()) :
            maxx = len(i.strip())

    print("*"*(maxx+4))
    for i in msg_group :
        print(f"* {i.strip():<{maxx}} *")
    print("*"*(maxx+4))
main()
