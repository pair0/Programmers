def solution(answers):
    answer = []
    N = len(answers)
    count = 0
    first = [0] * N
    second = [0] * N
    thrid = [0] * N
    ans_sc = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_th = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    while count < N:
        first[count] = (count % 5) + 1
        second[count] = ans_sc[count % 8]
        thrid[count] = ans_th[count % 10]
        count += 1

    firstCount = 0
    scondCount = 0
    thridCount = 0

    for i in range(len(answers)):
        if answers[i] == first[i]:
            firstCount += 1
        if answers[i] == second[i]:
            scondCount += 1
        if answers[i] == thrid[i]:
            thridCount += 1

    maxValue = max(firstCount, scondCount, thridCount)

    if maxValue == firstCount:
        answer.append(1)
    if maxValue == scondCount:
        answer.append(2)
    if maxValue == thridCount:
        answer.append(3)

    return answer
