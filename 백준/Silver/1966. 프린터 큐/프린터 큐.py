from collections import deque

t= int(input())
for _ in range(t):
    n,m = map(int,input().split())
    numbers = list(map(int,input().split()))
    f = numbers[m]
    q = deque()
    for i,n in enumerate(numbers):
        q.append((i,n))

    count =0
    for i in range(9,f,-1):
        max_ind = 0
        for d,(ind,num) in enumerate(q):
            if num == i:
                max_ind = d+1
                count+=1
        q.rotate(-max_ind)
    # print(q)
    for ind,num in q:
        if ind ==m and num ==f:
            print(count+1)
            break
        elif num ==f:
            count+=1

