def solution(polynomial):
    poly_list = polynomial.split(' + ')
    temp_one = 0
    temp_zero = 0

    for i in poly_list:
        if 'x' in i:
            if 'x' == i:
                temp_one += 1
            else:
                temp_one += int(i[:len(i)-1])  # x의 계수가 1자리가 아닐 수 있으므로 주의
        else:
            temp_zero += int(i)

    if temp_one > 1:
        if temp_zero != 0:
            answer = f'{temp_one}x + {temp_zero}'
        else:
            answer = f'{temp_one}x'
    elif temp_one == 1:
        if temp_zero != 0:
            answer = f'x + {temp_zero}'
        else:
            answer = f'x'
    elif temp_zero != 0:
        answer = f'{temp_zero}'
    else:
        answer = 0

    return answer
