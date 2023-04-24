def solution(s):
    answer = ''
    count = 0

    for i in s:
        if i == " ":
            count = 0
            answer += i
        elif count == 0:
            answer += i.upper()
            count += 1
        else:
            answer += i.lower()

    return answer
