"""
with open('sequence.txt', 'r') as fr:
    l = fr.read()
    a=l.count('A')
    t=l.count('T')
    g=l.count('G')
    c=l.count('C')
print "GC content: ",
"""
def calcGC(s):
    num_c=s.count("C")
    num_g=s.count("G")
    gc = float(num_c + num_g)/len(s)*100
    return gc

if __name__=="__main__":
    s=""
    with open("sequence.txt",'r') as fr:
        for line in fr:
            s += line.strip()
    print(s)
    gc = calcGC(s)
    print(gc)
