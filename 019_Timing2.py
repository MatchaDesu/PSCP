"Time II"
def main() :
    "main"
    sec = int(input())
    day,remain = divmod(sec,86400)
    if len(str(day)) <= 4 :
        hour,remain = divmod(remain,3600)
        minute,remain = divmod(remain,60)
        print(f"{day:>04}:{hour:>02}:{minute:>02}:{remain:>02}")
    else :
        print("ERR_:__:__:__")
main()
