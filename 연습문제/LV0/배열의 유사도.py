def solution(s1, s2):
    answer = 0

    if len(s1) <= len(s2):
        for i in s1:
            if i in s2:
                answer += 1
    elif len(s1) >= len(s2):
        for i in s2:
            if i in s1:
                answer += 1

    return answer
