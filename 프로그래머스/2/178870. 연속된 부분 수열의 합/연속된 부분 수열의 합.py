def solution(sequence, k):
    s = [0]
    for num in sequence:
        if not s:
            s.append(num)
        else:
            s.append(s[-1]+num)
    i = 0
    j = 0
    l = len(s)
    m = 10**9
    while i < l and j<l:
        if s[j] - s[i] <k:
            j+=1
        elif s[j] - s[i] == k:
            if j-i <m:
                m = j-i
                answer =[i,j-1]
            i+=1
            j+=1
        else:
            i+=1
    return answer