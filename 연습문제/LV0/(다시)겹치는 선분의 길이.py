# 교집합, 합집합 등등

def solution(lines):
    answer = 0
    sets = [set(range(min(l), max(l))) for l in lines]
    answer = len(sets[0] & sets[2] | sets[1] & sets[2] | sets[0] & sets[1])
    return answer
