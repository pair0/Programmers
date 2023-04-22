def solution(my_string):
    answer = ''
    gather = ['a', 'e', 'i', 'o', 'u']

    for i in my_string:
        if i not in gather:  # 모음을 제외한 문자가 나오면 answer에 추가
            answer += i

    return answer
