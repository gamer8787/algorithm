def solution(storey):
    m = 10**9
    def dfs(k,count):
        nonlocal m
        if k>10**8:
            return
        if k==0:
            m = min(m,count)
        else:
            s = str(k)
            for i,n in enumerate(s[::-1]):
                if n !="0":
                    nz = int(n)*(10**i)
                    break
            k1 = k-nz
            k2 = k-nz+10**(i+1)
            dfs(k1,count+int(n))
            dfs(k2,count+10-int(n))
    dfs(storey,0)
    answer = 0
    return m