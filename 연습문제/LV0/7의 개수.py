def solution(array):
    answer = 0
    # 리스트를 str로 변환 후(변환 이유 : int형이면 합쳐지지가 않는다...), 하나의 string으로 합친다.
    array = ''.join(list(map(str, array)))
    for i in array:
        if i == '7':
            answer += 1
    return answer
