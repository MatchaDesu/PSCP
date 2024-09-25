"Plan"
def ascend(a,b,c):
    "ascend"
    if a <= b <= c :
        print(f"{a:.2f}, {b:.2f}, {c:.2f}")
    elif a <= c <= b :
        print(f"{a:.2f}, {c:.2f}, {b:.2f}")
    elif b <= a <= c :
        print(f"{b:.2f}, {a:.2f}, {c:.2f}")
    elif b <= c <= a :
        print(f"{b:.2f}, {c:.2f}, {a:.2f}")
    elif c <= a <= b :
        print(f"{c:.2f}, {a:.2f}, {b:.2f}")
    elif c <= b <= a :
        print(f"{c:.2f}, {b:.2f}, {a:.2f}")

def descent(a,b,c):
    "descent"
    if a <= b <= c :
        print(f"{c:.2f}, {b:.2f}, {a:.2f}")
    elif a <= c <= b :
        print(f"{b:.2f}, {c:.2f}, {a:.2f}")
    elif b <= a <= c :
        print(f"{c:.2f}, {a:.2f}, {b:.2f}")
    elif b <= c <= a :
        print(f"{a:.2f}, {c:.2f}, {b:.2f}")
    elif c <= a <= b :
        print(f"{b:.2f}, {a:.2f}, {c:.2f}")
    elif c <= b <= a :
        print(f"{a:.2f}, {b:.2f}, {c:.2f}")

if input() == "Ascend" :
    ascend(float(input()),float(input()),float(input()))
else :
    descent(float(input()),float(input()),float(input()))
