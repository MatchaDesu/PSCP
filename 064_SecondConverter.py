"Second Converter"
def main(k,s,m,h) :
    "main"
    hour = k % (h*m*s)
    hour,minute = divmod(hour,m*s)
    minute,second = divmod(minute,s)
    print(f"{hour}:{minute}:{second}")
main(int(input()),int(input()),int(input()),int(input()))
