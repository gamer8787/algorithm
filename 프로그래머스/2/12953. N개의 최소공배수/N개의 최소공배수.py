def solution(arr):
    arr.sort()
    if len(arr) == 2:
        return lcm(arr[0],arr[1])
    else:
        a1 = lcm(arr[0],arr[1])
        new_arr = [a1, *arr[2:]]
        return solution(new_arr)

def lcm(a,b):
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            return a*b//i