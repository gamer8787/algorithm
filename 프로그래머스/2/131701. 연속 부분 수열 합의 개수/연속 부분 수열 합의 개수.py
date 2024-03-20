def solution(elements):
    length = len(elements)
    #dp[i][j] = j부터 i개의 합
    dp = [[0 for _ in range(length+1)] for _ in range(length+1)]
    for i in range(1,length+1):
        for j in range(length):
            dp[i][j] = dp[i-1][j] +elements[(i+j-1)%length]
    a = set()
    for i in range(1,length+1):
        for j in range(length):
            a.add(dp[i][j])
    return len(a)