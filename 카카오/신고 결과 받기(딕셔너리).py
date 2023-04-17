from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    hash_map = defaultdict(set)
    cnt = defaultdict(int)

    # 신고 리스트와 신고당한 횟수를 dict 형태로 작성
    for j in report:
        hash_map[j.split()[0]].add(j.split()[1])
        cnt[j.split()[1]] += 1

    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in hash_map[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)

    return answer
