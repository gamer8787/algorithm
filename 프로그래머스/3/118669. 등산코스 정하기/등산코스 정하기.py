from collections import deque


def solution(n, paths, gates, summits):
    INF = 10 **9
    summits.sort()
    set_gates = set(gates)
    set_summits = set(summits)
    edges = [[] for _ in range(n + 1)]
    for a, b, c in paths:
        edges[a].append((b, c))
        edges[b].append((a, c))
    def bfs(intense):
        visited = set_gates.copy()
        q = deque(gates)
        while q:
            v = q.popleft()
            for u,c in edges[v]:
                if u not in visited and c<=intense:
                    visited.add(u)
                    if u not in set_summits:
                        q.append(u)
        for e in summits:
            if e in visited:
                return e
        return 0
    start = 0
    end = 10000000
    s = 0
    while start+1<end: #fffeee
        mid = (start+end)//2
        summit = bfs(mid)
        if summit:
            end = mid
            s = summit
        else:
            start = mid
    # print(s,end)
    return [bfs(end),end]

# solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1,3],[5])
# solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3,7],[1,5])
