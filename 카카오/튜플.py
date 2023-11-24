def solution(s):
    answer = []
    listS = s[2:-2].split("},{")
    listS.sort(key=lambda x: len(x))
    count = 0
    for i in listS:
        if count == 0:
            answer.append(int(i))
        else:
            answer.append(list(set(map(int, i.split(","))) - set(answer))[0])
        count += 1

    return answer
