#menu : 음료 제조 시간
#order : 손님들이 주문한 음료
#k : 새로운 한 명의 손님이 방문하는데 걸리는 시간

def solution(menu, order, k):
    Len = len(order)
    peo_come = [i for i in range(0, Len*k, k)]
    peo_out = [0 for _ in range(Len)]
    peo_out[0] = menu[order[0]]
    max_answer = -1
    
    for i in range(1, Len):
        wait = 0
        if peo_out[i-1] > peo_come[i]:
            wait = peo_out[i-1] - peo_come[i]
        peo_out[i] = peo_come[i] + menu[order[i]] + wait
        
    for i in range(Len-2):
        answer = 1
        end = peo_out[i]
        for s, e in zip(peo_come[i+1:], peo_out[i+1:]):
            if s < end:
                answer += 1
            else:
                break
        if max_answer < answer:
            max_answer = answer
    
    return max_answer


# 더 짧은 방법
#menu : 음료 제조 시간
#order : 손님들이 주문한 음료
#k : 새로운 한 명의 손님이 방문하는데 걸리는 시간

def solution(menu, order, k):
    Len = len(order)
    peo_come = [i for i in range(0, Len*k, k)]
    peo_out = [0 for _ in range(Len)]
    peo_out[0] = menu[order[0]]
    max_answer = -1
    
    for i in range(1, Len):
        wait = 0
        if peo_out[i-1] > peo_come[i]:
            wait = peo_out[i-1] - peo_come[i]
        peo_out[i] = peo_come[i] + menu[order[i]] + wait
        
    # 시간대별로 들어오고 나가는 손님의 수를 추적하는 딕셔너리
    guest_count = {}
    
    # 모든 도착과 출발 시간을 기록하고 손님 수를 셉니다.
    for i in range(Len):
        arrival_time = peo_come[i]
        departure_time = peo_out[i]
        
        # 도착 시간에 손님 수를 1 증가시킵니다.
        if arrival_time in guest_count:
            guest_count[arrival_time] += 1
        else:
            guest_count[arrival_time] = 1
        
        # 출발 시간에 손님 수를 1 감소시킵니다.
        if departure_time in guest_count:
            guest_count[departure_time] -= 1
        else:
            guest_count[departure_time] = -1
    
    max_guests = 0  # 가장 많은 손님 수
    current_guests = 0  # 현재 카페에 있는 손님 수
    
    # 시간대별로 손님 수를 업데이트하면서 가장 많은 손님 수를 찾습니다.
    for time in sorted(guest_count.keys()):
        current_guests += guest_count[time]
        max_guests = max(max_guests, current_guests)
    
    return max_guests



