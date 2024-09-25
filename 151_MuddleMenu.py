"Muddled Menu"
def main() :
    "main"
    course = []
    menu = None
    while True :
        menu = input()
        if menu in "DONE" :
            break
        if menu in "CLOSED" :
            course.clear()
            break
        if menu in "SOMETHING'S WRONG" :
            course.clear()
        elif "Can't do:" in menu :
            menu = menu.split(": ")[1]
            course.remove(menu)
        else :
            menu,order = menu.split("#")
            if order in "N" :
                order = "-1"
                course.append(menu.strip())
            else :
                course.insert(int(order)-1, menu.strip())
    reverse = course.copy()
    reverse.reverse()
    print("Full Course:",course,"Reversed:",reverse)
main()
