import heapq
def solution(n, works):
    q = []
    for w in works:
        heapq.heappush(q,-w)
    for _ in range(n):
        a = heapq.heappop(q)
        if a == 0:
            return 0
        a+=1
        heapq.heappush(q,a)
    answer = 0
    for w in q:
        answer+=(w*w)
        
    return answer