import math

def enc(s):
    n=0
    st = math.ceil(math.sqrt(len(s)))
    res = ""
    for i in range (n,st):
        res+=s[n::st] + " "
        n+=1
    return res
s = input()
result =enc(s)


