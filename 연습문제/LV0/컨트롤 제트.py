def solution(s):
    answer = 0
    list_s = s.split()

    for i in range(len(list_s)):
        if list_s[i] == "Z":
            answer -= int(list_s[i-1])
        else:
            answer += int(list_s[i])

    return answer
