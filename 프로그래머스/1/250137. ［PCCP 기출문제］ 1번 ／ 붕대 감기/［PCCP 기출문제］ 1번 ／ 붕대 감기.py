def solution(bandage, health, attacks):
    maximum = health
    t,h,a = bandage
    last_time = attacks[-1][0]
    attack = [0 for _ in range(last_time+1)]
    for time,damage in attacks:
        attack[time] = damage
    sequence = 0
    for time in range(1,last_time+1):
        if attack[time] > 0:
            sequence = 0
            health -= attack[time]
            if health <= 0 :
                return -1
        else:
            sequence+=1
            health = min(health+h,maximum)
            if sequence == t:
                health = min(health+a,maximum)
                sequence = 0
        print(time,health)
    return health