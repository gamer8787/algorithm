from collections import deque
def solution(order):
    queue = [0 for _ in range(len(order))]
    for i,o in enumerate(order):
        queue[o-1] = i+1
    queue = deque(queue)
    stack = deque()
    count = 0
    while queue:
        if queue and queue[0] == count+1:
            count+=1
            queue.popleft()
        elif stack and stack[-1] == count+1:
            count+=1
            stack.pop()
        else:
            a = queue.popleft()
            stack.append(a)
    while stack:
        if stack[-1] == count+1:
            count+=1
            stack.pop()
        else:
            break
    return count