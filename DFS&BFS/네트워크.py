from collections import deque

# BFS


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    queue = deque()

    queue.append(0)

    for j in range(n):
        if not visited[j]:
            queue.append(j)
            while queue:
                visit = queue.popleft()

                for i in range(n):
                    if not visited[i] and computers[visit][i] == 1:
                        queue.append(i)
                        print(i)
                        visited[i] = True
            answer += 1

    return answer


# DFS


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1  # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer


def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:  # 연결된 컴퓨터
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
