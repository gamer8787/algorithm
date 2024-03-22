def solution(sticker):
    l = len(sticker)
    dp1 =[0 for _ in range(l)]
    dp1[0] = sticker[0]
    for i in range(1,l):
        if i ==l-1:
            dp1[i] = dp1[i-1]
            continue
        dp1[i] = max(dp1[i-2] + sticker[i],dp1[i-1])
    dp2 = [0 for _ in range(l)]
    for i in range(1,l):
        dp2[i] = max(dp2[i-2] + sticker[i],dp2[i-1])
    a = max(dp1)
    b = max(dp2)
        
    
    return max(a,b)