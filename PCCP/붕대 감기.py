from collections import defaultdict


# t초 동안 감으면서 1 -> +X -> (t초 연속으로 붕대) -> +y+x
def solution(bandage, health, attacks):
    answer = 0
    t, x, y = bandage[0], bandage[1], bandage[2]
    last_attack = attacks[-1][0]
    dic = defaultdict(int)
    flag = 0
    init_health = health

    for i, j in attacks:
        dic[i] = j

    for i in range(last_attack + 1):
        if dic[i] == 0:
            health += x
            flag += 1
            if flag == t:
                health += y  # 연속 성공 보너스
                flag = 0  # 연속 성공 초기화
            if health > init_health:
                health = init_health
        else:
            health -= dic[i]
            flag = 0

        if health <= 0:
            return -1

    return health
