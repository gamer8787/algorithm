dy = [-1,0,1,0]
dx = [0,1,0,-1]
from collections import deque
def solution(game_board, table):
    N = len(game_board)
    visited_board = [[False for _ in range(N)] for _ in range(N)]
    def bfs_board(i,j):
        ret = []
        visited_board[i][j] = True
        ret.append([i,j])
        q = deque()
        q.append((i,j))
        while q:
            i,j = q.popleft()
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<N and 0<=nj<N and game_board[ni][nj]==0 and visited_board[ni][nj]==False:
                    visited_board[ni][nj]=True
                    ret.append([ni,nj])
                    q.append((ni,nj))
        return ret
    
    visited_table = [[False for _ in range(N)] for _ in range(N)]
    def bfs_table(i,j):
        ret = []
        visited_table[i][j] = True
        ret.append([i,j])
        q = deque()
        q.append((i,j))
        while q:
            i,j = q.popleft()
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<N and 0<=nj<N and table[ni][nj]==1 and visited_table[ni][nj]==False:
                    visited_table[ni][nj]=True
                    ret.append([ni,nj])
                    q.append((ni,nj))
        return ret
    
    board_puzzle = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and visited_board[i][j] == False:
                r = bfs_board(i,j)
                board_puzzle.append(r)
    table_puzzle = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and visited_table[i][j] == False:
                r = bfs_table(i,j)
                table_puzzle.append(r)
    board_puzzle = [move(i) for i in board_puzzle]
    
   
    table_puzzle0 = [move(i) for i in table_puzzle]
    table_puzzle1 = [move(rotate(i)) for i in table_puzzle0]
    table_puzzle2 = [move(rotate(i)) for i in table_puzzle1]
    table_puzzle3 = [move(rotate(i)) for i in table_puzzle2]
    
    avail = set()
    count = 0
    for puzzle1 in board_puzzle:
        for i in range(len(table_puzzle)):
            if i in avail:
                continue
            if puzzle1 == table_puzzle0[i] or puzzle1 == table_puzzle1[i] or puzzle1 == table_puzzle2[i] or puzzle1 == table_puzzle3[i]:
                avail.add(i)
                count += len(puzzle1)
                break
    print(count)
    print(avail)
    answer = -1
    return count


def move(puzzle):
    puzzle.sort()
    r,c = puzzle[0]
    new_puzzle = []
    for a,b in puzzle:
        nr = a-r
        nc = b-c
        new_puzzle.append([nr,nc])
    return new_puzzle

def rotate(puzzle):
    new_puzzle = []
    for a,b in puzzle:
        nr = b
        nc = -a
        new_puzzle.append([nr,nc])
    return new_puzzle
    
    
    