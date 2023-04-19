def solution(num_list):
    oddNumber_count = 0
    even_count = 0

    for i in num_list:
        if i % 2 == 0:  # 짝수 개수
            even_count += 1
        else:  # 홀수 개수
            oddNumber_count += 1

    answer = [even_count, oddNumber_count]
    return answer
