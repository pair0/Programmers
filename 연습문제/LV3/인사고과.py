### 시간 초과
# def solution(scores):
#     answer = 1
#     N = len(scores)
    
#     OwanHo = scores[0]
#     scores = sorted(scores[1:])
#     scores.sort(key=lambda x:x[1])
#     list_N = list()
    
#     for i in range(0, N-2):
#         flag = 0
#         for j in range(i+1, N-1):
#             if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
#                 flag = 1
#                 break
#         if flag == 0:
#             list_N.append(scores[i])
            
#     list_N = sorted(list_N, reverse=True, key=lambda x:x[0]+x[1])

#     for i in range(len(list_N)):
#         if OwanHo[0] < list_N[i][0] and OwanHo[1] < list_N[i][1]:
#             answer = -1
#             break
#         elif OwanHo[0] + OwanHo[1] >= list_N[i][0] + list_N[i][1]:
#             break
#         else:
#             answer += 1
        
#     return answer

### 정답
def solution(scores):
    answer = 1
    N = len(scores)
    
    OwanHo = scores[0]
    scores = sorted(scores[1:], key=lambda x: (-x[0], x[1]))
    list_N = list()
    maxb = 0
    
    for i, j in scores:
        if OwanHo[0] < i and OwanHo[1] < j:
            return -1
        elif j >= maxb:
            maxb = j
            if i + j > sum(OwanHo):
                answer += 1
    return answer