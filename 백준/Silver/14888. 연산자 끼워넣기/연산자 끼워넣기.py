n = int(input())
numbers = list(map(int,input().split()))
op = list(map(int,input().split()))
#+-x//
INF = 10**9
m = INF
M = -INF
def dfs(op,numbers):
    global m,M
    if len(numbers) ==1:
        m = min(m,numbers[0])
        M = max(M, numbers[0])
    else:
        if op[0]>0:
            a = numbers[0] + numbers[1]
            new = [a, *numbers[2:]]
            new_op = op[:]
            new_op[0]-=1
            dfs(new_op,new)
        if op[1]>0:
            a = numbers[0] - numbers[1]
            new = [a, *numbers[2:]]
            new_op = op[:]
            new_op[1]-=1
            dfs(new_op,new)
        if op[2]>0:
            a = numbers[0] * numbers[1]
            new = [a, *numbers[2:]]
            new_op = op[:]
            new_op[2]-=1
            dfs(new_op,new)
        if op[3]>0:
            if numbers[0] > 0:
                a = numbers[0] // numbers[1]
            else:
                a= -((-numbers[0]) // numbers[1])
            new = [a, *numbers[2:]]
            new_op = op[:]
            new_op[3]-=1
            dfs(new_op,new)
dfs(op,numbers)
print(M)
print(m)