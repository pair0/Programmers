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