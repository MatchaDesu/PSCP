"Future Message"
msg = input()
if msg.isnumeric() :
    print("Number")
elif msg.isupper() :
    print("Uppercase")
elif msg.islower() :
    print("Lowercase")
elif msg.istitle() :
    print("Title")
elif msg.isspace() :
    print("Space")
else :
    print("Other")
