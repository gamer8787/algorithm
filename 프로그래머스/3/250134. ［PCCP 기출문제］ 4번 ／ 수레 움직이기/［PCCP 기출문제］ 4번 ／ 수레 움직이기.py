from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solution(maze):
    r = len(maze)
    c = len(maze[0])
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 1:
                red = (i,j)
            elif maze[i][j] == 2:
                blue = (i,j)
            elif maze[i][j] == 3:
                red_target = (i,j)
            elif maze[i][j] == 4:
                blue_target = (i,j)

    def candidate(cur, visited, target):
        ret = []
        if cur == target:
            return [cur]
        y,x = cur
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<r and 0<=nx<c and (ny,nx) not in visited and maze[ny][nx]!= 5:
                ret.append((ny,nx))
        return ret

    minimum  = 10 **9
    def bf(red,blue,turn,red_visited,blue_visited):
        nonlocal minimum
        if red == red_target and blue == blue_target:
            minimum = min(turn,minimum)
            return
        red_can = candidate(red,red_visited,red_target)
        blue_can = candidate(blue,blue_visited,blue_target)
        for new_red in red_can:
            for new_blue in blue_can:
                if new_blue== new_red or (new_red==blue and new_blue == red):
                    continue
                else:
                    new_red_visited = red_visited | {new_red}
                    new_blue_visited = blue_visited | {new_blue}
                    bf(new_red,new_blue,turn+1,new_red_visited,new_blue_visited)
    red_visited = {red}
    blue_visited = {blue}
    bf(red,blue,0,red_visited,blue_visited)
    print(minimum)
    if minimum == 10**9:
        return 0
    else:
        return minimum

solution([[1, 4], [0, 0], [2, 3]])