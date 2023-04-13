# 75점....
import heapq
from collections import defaultdict
from collections import deque


def solution(tickets):
    answer = []
    n = len(tickets)
    tickets.sort()
    queue = deque()
    visited = [False for _ in range(n)]

    for start in range(n):
        if tickets[start][0] == 'ICN' and False in visited:
            visited = [False for _ in range(n)]
            answer = []
            queue.append(start)
            visited[start] = True
            answer.append(tickets[start][0])
            bfs(tickets, queue, visited, answer, start)

    return answer


def bfs(tickets, queue, visited, answer, start):
    count = 0
    while queue:
        visit = queue.popleft()
        for i in range(len(tickets)):
            if tickets[visit][1] == tickets[i][0] and not visited[i]:
                queue.append(i)
                visited[i] = True
                answer.append(tickets[i][0])
                count += 1
                if count + 1 == len(tickets):
                    answer.append(tickets[i][1])
                break


# 100점


def solution(tickets):
    r = defaultdict(list)

    for i, j in tickets:
        r[i].append(j)
        print(r)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]


# 만점 짜리


def solution(tickets):
    answer = []
    graph = {}
    # 그래프 초기화
    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

    # 도착지를 알파벳 역순으로 정렬
    for key in graph.keys():
        graph[key].sort(reverse=True)

    # DFS
    stack = ["ICN"]
    while stack:
        current = stack[-1]
        if current not in graph or len(graph[current]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[current].pop())

    # 경로 뒤집기
    answer.reverse()

    return answer
