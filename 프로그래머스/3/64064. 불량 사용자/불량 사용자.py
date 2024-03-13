from itertools import combinations,permutations
def solution(user_id, banned_id):
    per = permutations(banned_id)
    comb = combinations(user_id,len(banned_id))
    ret = 0
    for c in comb:
        for p in permutations(banned_id):
            # print(p)
            if same_all(c,p):
                ret+=1     
                break
    print(ret)
    return ret

def same(a,b):
    if len(a)!=len(b):
        return False
    else:
        for i,j in zip(a,b):
            if j=="*":
                continue
            if i!=j:
                return False
    return True

def same_all(users,bans):
    for u,b in zip(users,bans):
        if not same(u,b):
            return False
    return True