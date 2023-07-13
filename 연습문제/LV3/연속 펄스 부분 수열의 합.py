### 시간 초과
from itertools import combinations

def solution(sequence):
    answer = 0
    N = len(sequence)
    answer_list = [0] * N
    answer_list_reverse = [0] * N
    answer_list[0] = sequence[0]
    answer_list_reverse[0] = -sequence[0]
    
    for i in range(1, len(sequence)):
        if i % 2 == 0:
            total = sequence[i] * 1
            total_reverse = sequence[i] * -1
        else:
            total = sequence[i] * -1
            total_reverse = sequence[i] * 1
            
        answer_list[i] = answer_list[i-1] + total
        answer_list_reverse[i] = answer_list_reverse[i-1] + total_reverse
    
    answer = max(answer_list + answer_list_reverse)
    
    for j, i in combinations(range(N), 2):
        temp = answer_list[i] - answer_list[j]
        temp1 = answer_list_reverse[i] - answer_list_reverse[j]

        if temp < temp1:
            temp = temp1

        if answer < temp:
            answer = temp

### 정답
from sys import maxsize

INF = maxsize

def solution(sequence):
    answer = -INF
    size = len(sequence)
    s1 = s2 = 0				# 1 
    s1_min = s2_min = 0		# 2
    pulse = 1
    
    for i in range(size):
        s1 += sequence[i] * pulse
        s2 += sequence[i] * (-pulse)
        
        # 3 가장 작은 값을 빼야 큰값이 도출
        answer = max(answer, s1-s1_min, s2-s2_min)
        
        # 4 
        s1_min = min(s1_min, s1)
        s2_min = min(s2_min, s2)
        
        # 5 펄스 값 바꾸기
        pulse *= -1
    return answer