"Iphone 13 Again!?"
storage = ("128 GB","256 GB","512 GB","1 TB")
product_name = ("iPhone 13 mini","iPhone 13","iPhone 13 Pro","iPhone 13 Pro Max")
ip13_mini = (25900,29900,37900,"Not Available")
ip_13 = (29900,33900,41900,"Not Available")
ip13_pro = (38900,42900,50900,58900)
ip13_promax = (42900,46900,54900,62900)
product_list = (ip13_mini,ip_13,ip13_pro,ip13_promax)

def main() :
    "main"
    name = input()
    memory = input()
    if name in product_name and memory in storage :
        print(product_list[product_name.index(name)][storage.index(memory)])
    else :
        print("Not Available")
main()
