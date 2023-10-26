# 1. 모든 판매원은 칫솔의 판매에 의하여 발생하는 이익에서 10%를 계산하여 => 추천인에게 배분
# 2. 90%는 자신이 갖는다. or 자신이 조직에 추천하여 가입시킨 판매원에게서 10% 받는다.
# 3. 10%를 계산할 때에는 원 단위에서 절사, 10%를 계산한 금액이 1원 미만일 경우 이득 분배X
# 4. 칫솔 개당 100원 고정
# enroll : 각 판매원의 이름이 담김 (민호 제외) (조직에 참여한 순서)
# referral : 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 (-은 추천인 없음 민호 한테만 이득이 감)
# seller :  판매량 집계 데이터의 판매원 이름을 나열한 배열
# amount : 판매량 집계 데이터의 판매 수량을 나열한 배열

from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    graph = defaultdict(str)
    people = defaultdict(int)
    people["minho"] = 0

    for enr, refer in zip(enroll, referral):
        people[enr] = 0
        if refer == "-":
            graph[enr] = "minho"
        else:
            graph[enr] = refer

    for i in range(len(seller)):
        people[seller[i]] += amount[i] * 90
        sel = seller[i]
        remain = amount[i] * 10

        while 1:
            hi = graph[sel]
            tmp = remain

            if hi == "minho" or remain < 1:
                break

            remain = int(remain * 0.1)
            people[hi] += tmp - remain
            sel = hi

    for k, v in people.items():
        answer.append(v)

    return answer[1:]
