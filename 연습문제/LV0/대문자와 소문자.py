def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():  # 대문자인지 판단
            answer += i.lower()  # 대문자이면 소문자로 변환해서 저장
        else:
            answer += i.upper()

    return answer
