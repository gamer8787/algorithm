dy = [-1,0,1,0]
dx = [0,1,0,-1]

import heapq
from collections import deque,defaultdict
def solution(land, height):
    n = len(land)
    color_graph = [[0 for _ in range(n)] for _ in range(n)]
    def bfs(i,j,color):
        visited[i][j] = True
        q = deque()
        q.append((i,j))
        while q:
            i,j = q.popleft()
            color_graph[i][j] = color
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<n and 0<=nj<n and visited[ni][nj] == False:
                    if abs( land[ni][nj] - land[i][j]) <=height:
                        visited[ni][nj] = True
                        q.append((ni,nj))

    visited = [[False for _ in range(n)] for _ in range(n)]
    color = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i,j,color)
                color+=1
    INF = 10**9
    edge = defaultdict(lambda :INF)
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i +dy[k]
                nj = j +dx[k]
                if 0<=ni<n and 0<=nj<n and color_graph[ni][nj] != color_graph[i][j]:
                    c1 = color_graph[ni][nj]
                    c2 = color_graph[i][j]
                    distance = abs( land[ni][nj]-land[i][j] )
                    edge[(c1,c2)] = min(edge[(c1,c2)] , distance)
                    edge[(c2,c1)] = min(edge[(c2,c1)] , distance)
    # for g in color_graph:
    #     print(g)
    # for e in edge:
    #     print(e)

    edges = []
    for i,j in edge:
        heapq.heappush(edges,(edge[(i,j)],i,j))
    # print(edges)
    parent = [i for i in range(color+1)]

    ret = 0
    count = 0
    while edges:
        c,a,b = heapq.heappop(edges)
        if find(a,parent)!=find(b,parent):
            union(a,b,parent)
            ret+=c
            count+=1

    return ret

def find(x,parent):
    if x!=parent[x]:
        parent[x] = find(parent[x],parent)
    return parent[x]

def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b