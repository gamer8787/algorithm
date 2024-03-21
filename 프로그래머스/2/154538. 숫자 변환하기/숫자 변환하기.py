from collections import deque
def solution(x, y, n):
    visited = [-1 for _ in range(y+1)]
    visited[x] = 0
    q = deque()
    q.append(x)
    while q:
        v = q.popleft()
        for u in [2*v,3*v,v+n]:
            if u <=y and visited[u] ==-1:
                visited[u] = visited[v]+1
                q.append(u)
    return visited[y]