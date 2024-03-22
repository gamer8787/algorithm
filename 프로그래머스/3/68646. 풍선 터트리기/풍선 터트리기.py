def solution(a):
    dp1 = []
    INF = 10**9
    m = INF
    for me in a:
        if m < me:
            dp1.append(1)
        else:
            m = me
            dp1.append(0)


    dp2 = []
    m = INF
    for me in a[::-1]:
        if m <me:
            dp2.append(1)
        else:
            m = me
            dp2.append(0)
    dp2 = dp2[::-1]

    count = 0
    for i,j in zip(dp1,dp2):
        if i+j<=1:
            count+=1
    return count