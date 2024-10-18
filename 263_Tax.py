"Tax"
def main() :
    "main"
    year = int(input())
    size = int(input())
    total = 0

    if size > 0 :
        total += min(size,600)*0.5

    if size > 600 :
        total += (min(size,1800)-600)*1.5

    if size > 1800 :
        total += (size-1800)*4

    total *= (100 - (max(0,year-5)*10))/100 if year <= 10 else 50/100

    print(f"{total:.2f}")
main()
