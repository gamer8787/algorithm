def solution(numbers):
    answer = []
    for n in numbers:
        if n %2==0:
            answer.append(n+1)
        else:
            c = 0 #1연속 개수
            a = bin(n)[2:]
            for i in a[::-1]:
                if i =="1":
                    c+=1
                else:
                    break
            answer.append(n+2**(c-1))
    return answer