from collections import deque


# 우선순위 : 1~10 -> 낮을수록 우선순위 높다
def solution(program):
    queue = deque()
    answer = [0] * 11
    sum_pro = 0
    for i in range(len(program)):
        sum_pro += program[i][2]

    program = sorted(program, key=lambda x: x[0])
    program = sorted(program, key=lambda x: x[1])
    queue.append((0, *program[0]))
    program.pop(0)
    flag = 0

    while queue:
        flag2 = 0
        input_t, i, s, t = queue.popleft()  # 실행 시간, 점수, 호출된 시간, 실행
        answer[i] += input_t - s  # 대기 시간
        if len(program) == 0:
            break

        quqlist = []
        for k in range(len(program)):
            if program[k][1] <= t:
                quqlist.append([program[k][0], program[k][1], program[k][2]])
                flag2 = 1
            elif program[k][1] > t and flag2 == 0:
                break

        if flag2 == 1:
            quqlist.sort(key=lambda x: x[0])
            queue.append((t, quqlist[0][0], quqlist[0][1], t + quqlist[0][2]))
            for i in range(len(program)):
                if program[i] == quqlist[0]:
                    program.pop(i)
                    break
            flag += 1
        else:
            queue.append(
                (
                    program[0][1],
                    program[0][0],
                    program[0][1],
                    program[0][1] + program[k][2],
                )
            )
            program.pop(0)
            flag += 1

    answer[0] = t

    return answer


import heapq


def solution(program):
    answer = [0] * 11  # 프로그램 우선순위는 1~10번까지 존재하므로 (answer[0]은 최종 실행 시간)
    program.sort(key=lambda x: x[1])
    heap = []  # heapq의 경우 리스트를 사용해야 함
    cur = 0  # 현재 시각

    def call_program():  # program 배열 안의 프로그램을 pQ에 넣어주는 작업
        while len(program) > 0 and program[0][1] <= cur:
            heapq.heappush(heap, program.pop(0))

    cur = 0
    while len(program) > 0 or not len(heap) == 0:
        if len(heap) == 0:  # pQ가 비어있다면
            cur = program[0][1]  # program 배열의 맨 앞의 값의 시각을 현재 시각으로 설정
            call_program()
        execute = heapq.heappop(heap)  # 가장 앞의 값을 제거
        answer[execute[0]] += cur - execute[1]  # answer 배열의 해당 우선순위 인덱스에 대기 시간 값을 추가함
        cur += execute[2]  # 현재 시각을 갱신
        call_program()

    answer[0] += cur  # answer[0]은 모든 프로그램이 종료되는 시각

    return answer
