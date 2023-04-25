def solution(s):
    answer = ''

    for i in s:
        if s.count(i) == 1:
            answer += i

    answer = sorted(list(answer))  # 문자를 사전 순으로 정렬
    answer = ''.join(answer)  # 정렬된 문자열 배열을 join

    return answer
