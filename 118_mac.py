"Mac Address"
def main() :
    "main"
    sixteen_bit = "0123456789ABCDEF"
    address = input().upper()
    if address.count("-") :
        check = address.split("-")
        for i in check :
            for j in i :
                if len(i) != 2 or j not in sixteen_bit or len(check) != 6 or len(address) != 17:
                    print("ERROR")
                    return
        print("VALID 1")
        return
    if address.count(":") :
        check = address.split(":")
        for i in check :
            for j in i :
                if len(i) != 2 or j not in sixteen_bit or len(check) != 6 or len(address) != 17 :
                    print("ERROR")
                    return
        print("VALID 2")
        return
    if address.count(".") :
        check = address.split(".")
        for i in check :
            for j in i :
                if len(i) != 4 or j not in sixteen_bit or len(check) != 3 or len(address) != 14 :
                    print("ERROR")
                    return
        print("VALID 3")
        return
    print("ERROR")
main()
