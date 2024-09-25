"Brick"
def main(a,b,goal):
    "main"
    brick = goal - b*5
    if b*5 > goal :
        left = goal // 5
        brick = goal - left*5
    if brick <= a :
        print(brick)
    else :
        print(-1)

main(int(input()),int(input()),int(input()))
