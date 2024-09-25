"For!F-Ball"
msg = input()
a,b,c = 1,0,0
for i in msg :
    if i == "A" :
        a,b = b,a
    elif i == "B" :
        b,c = c,b
    else :
        a,c = c,a

cup = a,b,c

for i,char in enumerate(cup):
    if char :
        print(i+1)
