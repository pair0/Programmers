def solution(array):
    answer = 0
    max = -1
    flag = 0
    array_set = set(array)

    for i in array_set:
        if max < array.count(i):
            flag = 0  # 최빈값이 바뀌면 flag = 0으로 다시 셋팅
            max = array.count(i)
            answer = i
        elif max == array.count(i):  # 최빈값이 여러개이면 flag = 1로 셋팅
            flag = 1

    if flag == 1:  # flag가 1이면 결과 -1
        answer = -1

    return answer

# from collections import Counter

# def solution(array):
#     cnt = dict(Counter(array))
#     modes = sorted(cnt.items(), reverse = True, key=lambda x:x[1])
#     # modes = cnt.most_common()  # 빈도수가 높은 값부터 정렬된 리스트 반환
#     if len(array) == 1 or modes[0][1] != modes[1][1]:  # 최빈값이 유일하면서 그 값이 2번째로 높은 값과 같지 않을 때
#         return modes[0][0]  # 최빈값 반환
#     else:
#         return -1  # 최빈값이 여러 개인 경우 -1 반환
