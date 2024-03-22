def solution(n):
    a = ""
    while n>0:
        d = n//3
        r = n%3
        if r ==0:
            r=3
            d-=1
        a+=str(r)
        n = d
    a = a[::-1]
    a = a.replace("3","4")

    return a