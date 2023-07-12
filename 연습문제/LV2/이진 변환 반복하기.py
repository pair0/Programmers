def solution(s):
    answer = [0, 0]

    while s != "1":
        zero = s.count('0')
        s = s.replace('0', '')
        answer[1] += zero
        length = len(s)
        s = bin(length)[2:]
        answer[0] += 1

    return answer
