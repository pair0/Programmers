def solution(money):
    ice_cof = 5500
    answer = [money//ice_cof, money - ((money//ice_cof) * ice_cof)]

    return answer
