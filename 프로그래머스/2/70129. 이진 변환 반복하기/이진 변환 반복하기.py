def solution(s):
    stage =0
    zero =0
    while s!="1":
        stage+=1
        new =""
        for c in s:
            if c=="1":
                new+=c
            if c=="0":
                zero+=1
        new = len(new)
        s = bin(new)[2:]
        print(s)
    answer = [stage,zero]
    return answer