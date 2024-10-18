"Digit v2"
def main(txt) :
    "main"
    if "thousand" in txt :
        return 4
    if "hundred" in txt :
        return 3
    if "ty" in txt or "teen" in txt or "twelve" in txt or "eleven" in txt or "ten" in txt:
        return 2
    return 1
print(main(input()))
