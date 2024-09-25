"myMath"
import math
def main() :
    "main"
    a = math.sin(math.radians(90)) + (math.sin(math.radians(60)))**2
    a = a / (math.cos(math.radians(245**2)) + math.cos(math.radians(180)))
    b = (math.factorial(16)*math.factorial(4))/math.factorial(8)
    c = 40 / (math.sqrt(178))
    d = math.log10(1234**4)
    e = math.log(4234,5) + math.log2(8191) + 71*math.log10(156154)
    e = e / (math.log(777,7) - math.log(888,8) - math.log(999,9))
    print(a,b,c,d,e,sep="\n")
main()
