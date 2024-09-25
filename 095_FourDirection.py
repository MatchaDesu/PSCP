"Four Direction"
def main() :
    "main"
    button = input()
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    fifth_line = ""
    for i in button :
        if i == "U" :
            first_line  += "  *   "
            second_line += " ***  "
            third_line  += "* * * "
            fourth_line += "  *   "
            fifth_line  += "  *   "
        elif i == "L" :
            first_line  += "  *   "
            second_line += " *    "
            third_line  += "***** "
            fourth_line += " *    "
            fifth_line  += "  *   "
        elif i == "R" :
            first_line  += "  *   "
            second_line += "   *  "
            third_line  += "***** "
            fourth_line += "   *  "
            fifth_line  += "  *   "
        elif i == "D" :
            first_line  += "  *   "
            second_line += "  *   "
            third_line  += "* * * "
            fourth_line += " ***  "
            fifth_line  += "  *   "
    print(first_line,second_line,third_line,fourth_line,fifth_line,sep="\n")
main()
