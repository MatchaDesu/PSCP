"Largest number"
def ordering(a,b,c):
    "Find The Largest number"
    abc = str(a) + str(b) + str(c)
    acb = str(a) + str(c) + str(b)
    bac = str(b) + str(a) + str(c)
    bca = str(b) + str(c) + str(a)
    cab = str(c) + str(a) + str(b)
    cba = str(c) + str(b) + str(a)
    if int(abc) >= int(acb) :
        x = abc
    else :
        x = acb
    if int(bac) >= int(bca) :
        y = bac
    else :
        y = bca
    if int(cab) >= int(cba) :
        z = cab
    else :
        z = cba
    return x, y, z

def low_to_high(a,b,c):
    "Ordering The number"
    most = 0
    if int(a) <= int(b) <= int(c) :
        most = int(c)
    elif int(a) <= int(c) <= int(b) :
        most = int(b)
    elif int(b) <= int(a) <= int(c) :
        most = int(c)
    elif int(b) <= int(c) <= int(a) :
        most = int(a)
    elif int(c) <= int(a) <= int(b) :
        most = int(b)
    elif int(c) <= int(b) <= int(a) :
        most = int(a)
    return most

def main(a,b,c):
    "main"
    x,y,z = ordering(a,b,c)
    most = low_to_high(x,y,z)
    print(most)
main(int(input()),int(input()),int(input()))
