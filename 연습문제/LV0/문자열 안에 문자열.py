def solution(str1, str2):
    answer = 0
    # str1 안에 str2가 있으면 answer = 1, (문자열도 리스트와 같은 역할을 수행할 수 있다.)
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer
