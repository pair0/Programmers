def solution(array, n):
    answer = 101
    min_value = 101

    for i in array:
        print(abs(n-i))
        if abs(n-i) < min_value:
            min_value = abs(n-i)
            answer = i
        elif abs(n-i) == min_value:  # 가장 가까운 수가 여러 개일 경우 더 작은 수를 return
            if i < answer:
                answer = i

    return answer
