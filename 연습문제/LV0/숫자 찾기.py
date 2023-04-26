def solution(num, k):
    answer = 0
    num = list(str(num))

    if str(k) in num:
        answer = num.index(str(k)) + 1
    else:
        answer = -1

    return answer
