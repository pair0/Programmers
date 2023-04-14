def solution(array, commands):
    answer = []

    for n in commands:
        array_c = sorted(array[n[0]-1:n[1]])
        print(array_c)
        answer.append(array_c[n[2]-1])
    return answer
