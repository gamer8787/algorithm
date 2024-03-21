from collections import defaultdict
def solution(n, stations, w):
    before = 0
    length = []
    for s in stations:
        left = s-w
        right = s+w
        l = left - before-1
        if l >=1:
            length.append(l)
        before = right
    l = n - before
    if l >=1:
            length.append(l)
    
    require = 0
    scope = 2*w+1
    for l in length:
        require += (l//scope)
        if l%(scope) !=0:
            require+=1
    return require

    