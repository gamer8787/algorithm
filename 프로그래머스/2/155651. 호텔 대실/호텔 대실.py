def solution(book_time):
    dp = [0 for _ in range(24*60)]
    for a,b in book_time:
        a = change(a)
        b = change(b)
        dp[a]+=1
        dp[min(b+10,24*60-1)]-=1
    for i in range(1,24*60):
        dp[i] = dp[i-1] + dp[i]

    return max(dp)

def change(time):
    h,m = time.split(":")
    return 60*int(h)+int(m)