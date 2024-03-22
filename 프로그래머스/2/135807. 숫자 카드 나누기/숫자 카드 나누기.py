import sys
sys.setrecursionlimit(10**6)
def solution(arrayA, arrayB):
    gcdA = gcd_list(arrayA)
    gcdB = gcd_list(arrayB)
    
    m = 0
    if nodivide(gcdA,arrayB):
        m = max(m,gcdA)
    if nodivide(gcdB,arrayA):
        m = max(m,gcdB)
    
    return m

def nodivide(a,l):
    for i in l:
        if i%a==0:
            return False
    return True

def gcd_list(l):
    g = l[0]
    for i in range(len(l)):
        g = gcd(g,l[i])
    return g
def gcd(a,b):
    if a<=b:
        c = b%a
        if c ==0:
            return a
        else:
            return gcd(a,c)
    else:
        c = a%b
        if c ==0:
            return b
        else:
            return gcd(b,c)

    