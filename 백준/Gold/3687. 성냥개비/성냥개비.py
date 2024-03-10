t = int(input())
count = [6,2,5,5,4,5,6,3,7,6]
        #0,1,2,3,4,5,6,7,8,9
        #


#가장 작은 수
#2=>1을써야됨
#3=>7을써야됨
#4=>4를 써야됨
#5=>2를 써야됨
#6=>0,6을 써야됨
#7=>8을 써야됨

#1 x
#2 1
#3 7
#4 4
#5 2
#6 6 0
#7 8

#8 10
#9 18
#10 22 04
#11 20
#12 28 00
#13 68 08
#14 88

#15 108
#16 188
#17 200 ** 002
#18 208
#19 288
#20 688 088
#21 888

#22 1088
#23 1888
#24 2288
#25 2688 2088
#26 2888
#27 6888 0888
#28 8888

#29

dp = ["" for _ in range(101)]
dp0 = ["" for _ in range(101)]
dp0[:8] = ["0","0","1","7","4","2","0","8"]  #0으로 시작하는 것 가능
dp[:8] = ["0","0","1","7","4","2","6","8"]   #0으로 시작하지 않는 것중 가장 작음

for i in range(8, 101):
    if i % 7 == 0:
        dp0[i] = "8" + dp0[i - 7]
    elif i % 7 in [1, 2]:
        dp0[i] = "1" + dp0[i - 2]
    elif i % 7 in [3, 4, 5]:
        a = "2" + dp0[i-5]
        b = "0" + dp0[i-6]
        if len(a) < len(b):
            dp0[i] = a
        else:
            dp0[i] = b
    elif i % 7 in [6]:
        dp0[i] = "0" + dp0[i - 6]
# for i in range(30):
#     print(i,dp0[i])

for i in range(8,101):
    if i%7 == 0:
        dp[i] = "8" +dp0[i-7]
    elif i%7 in [1,2]:
        dp[i] = "1" + dp0[i-2]
    elif i%7 in [3,4,5]:
        a = "2" + dp0[i - 5]
        dp[i] = a
    elif i%7 in [6]:
        dp[i] = "6" +dp0[i-6]
# for i in range(30):
#     print(i,dp[i])

# print(dp)
#가장 큰수
# 짝수개다=>1로 도배
#홀수개다=>7하고 나머지 1로 도배
for _ in range(t):
    n = int(input())
    minimum = int(dp[n])
    if n % 2 ==0:
        maximum = int("1" * (n//2))
    else:
        maximum = int("7" + "1" * (n // 2 -1))
    print(minimum,maximum)






