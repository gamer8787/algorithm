def solution(n):
    answer = 0
    for k in range(1,501):
        first = k*(k+1)//2
        if n>=first and (n-first)%k==0:
            answer+=1
    
    return answer