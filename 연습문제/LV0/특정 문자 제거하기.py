def solution(my_string, letter):
    answer = ''

    for i in my_string:
        if i == letter:  # 삭제할 문자열과 같을 시 answer에 추가하지 않고 진행
            continue
        answer += i
    return answer
