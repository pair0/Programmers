# 교집합, 합집합 등등
from itertools import combinations

def solution(lines):
    answer = 0
    temp = set()
    sets = [set(range(min(l), max(l))) for l in lines]
    
    for i in combinations(sets, 2):
        temp |= i[0] & i[1]
        
    answer = len(temp)
        
    return answer
