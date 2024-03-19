def solution(n, s):
    if n > s:
        return [-1]
    a = s//n
    r = s%n
    answer = [a for _ in range(n)]
    for i in range(1,r+1):
        answer[-i]+=1
    return answer