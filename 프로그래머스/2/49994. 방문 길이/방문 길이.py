dy = [-1,0,1,0]
dx = [0,1,0,-1]
d = {"U" : (-1,0) ,"R" : (0,1) ,"D" : (1,0) ,"L" : (0,-1) }
def solution(dirs):
    visited = set()
    y = 0
    x = 0 
    count = 0
    for di in dirs:
        ny = y + d[di][0]
        nx = x + d[di][1]
        if -5<=ny<=5 and -5<=nx<=5:
            a = frozenset([(ny,nx),(y,x)])
            if a not in visited:
                count+=1
                visited.add(a)
            y = ny
            x = nx
    return count