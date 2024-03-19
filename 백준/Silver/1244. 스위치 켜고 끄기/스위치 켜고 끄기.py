n = int(input())
switch = list(map(int,input().split()))
s = int(input())
for _ in range(s):
    mf, num = map(int,input().split())
    if mf ==1:
        for i in range(n):
            if (i+1)%num == 0:
                switch[i] = 1 - switch[i]
    elif mf ==2:
        left = num-2
        right = num
        switch[num-1] = 1-switch[num-1]
        while 0<=left and right<n:
            if switch[left] == switch[right]:
                switch[left] = 1 - switch[left]
                switch[right] = 1 - switch[right]
            else:
                break
            left-=1
            right+=1
for i,n in enumerate(switch):
    if i>=20 and i%20 ==0:
        print()
    print(n,end=" ")
     
