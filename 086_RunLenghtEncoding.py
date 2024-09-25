"Run Lenght Encoding"
def main():
    "main"
    txt = input()
    end_txt = ""
    count = 1
    for i in range(1, len(txt)):
        if txt[i] == txt[i-1]:
            count += 1
        else:
            end_txt += str(count)+txt[i-1]
            count = 1
    end_txt += str(count)+txt[-1]
    print(end_txt)
main()
