def solution(num, total):
    temp = total // num

    if num % 2 != 0:
        answer = [i for i in range(temp-(num//2), temp+(num//2)+1)]
    else:
        answer = [i for i in range(temp-(num//2)+1, temp+(num//2)+1)]

    return answer
