def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        r = i//n
        c = i%n
        if c<=r:
            answer.append(r+1)
        else:
            answer.append(c+1)

    return answer