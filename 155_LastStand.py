"LastStand"
import json
def main() :
    "main"
    num = json.loads(input())
    num = map(str , num)
    for i in num :
        print(i[-1])
main()
