from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

INF = 10**9
def solution(board):
    N = len(board)
    #bfs
    visited = [[[INF,INF,INF,INF] for _ in range(N)] for _ in range(N)]
    visited[0][0] = [0,0,0,0]
    q = deque()
    q.append((0,0,-1))
    while q:
        i,j,d = q.popleft()
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if d == -1:
                cost = 100
            elif d==k:
                cost = 100
            else:
                cost = 600
            if 0<=ni<N and 0<=nj<N and board[ni][nj]==0 and visited[ni][nj][k] > visited[i][j][d] + cost:
                visited[ni][nj][k] = visited[i][j][d] + cost
                q.append((ni,nj,k))
    return min(visited[N-1][N-1])