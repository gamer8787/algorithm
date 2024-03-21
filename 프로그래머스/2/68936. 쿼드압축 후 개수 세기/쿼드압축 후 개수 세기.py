import sys
sys.setrecursionlimit(10**7)
def solution(arr):
    if len(arr)==1:
        a = arr[0][0]
        if a ==1:
            return [0,1]
        else:
            return [1,0]
    else:
        length = len(arr)//2
        a1 = solution([i[:length] for i in arr[:length]])
        a2 = solution([i[:length] for i in arr[length:]])
        a3 = solution([i[length:] for i in arr[:length]])
        a4 = solution([i[length:] for i in arr[length:]])
        if a1==a2==a3==a4==[1,0]:
            return [1,0]
        elif a1==a2==a3==a4==[0,1]:
            return [0,1]
        else:
            a = a1[0] + a2[0] + a3[0] + a4[0]
            b = a1[1] + a2[1] + a3[1] + a4[1]
            return [a,b]