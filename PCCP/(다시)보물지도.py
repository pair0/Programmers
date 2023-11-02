# x: n, y: m
# 한칸 이동 : 1, 놀라운 신발 : 두칸의 1 - 장애물도 넘어감(한번만 사용 가능)
from collections import deque


def solution(n, m, hole):
    answer = 0
    graph = [[0] * n for i in range(m)]
    for i, j in hole:
        graph[j - 1][i - 1] = 1

    queue = deque([(0, 0, False)])
    visited = [[[False] * 2 for _ in range(n)] for _ in range(m)]
    visited[0][0][False] = True

    # 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        for _ in range(len(queue)):
            x, y, use = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and not visited[ny][nx][use]
                    and graph[ny][nx] == 0
                ):
                    if (nx, ny) == (n - 1, m - 1):
                        return answer + 1
                    queue.append((nx, ny, use))
                    visited[ny][nx][use] = True
                if not use:
                    nx += dx[i]
                    ny += dy[i]
                    if (
                        0 <= nx < n
                        and 0 <= ny < m
                        and not visited[ny][nx][True]
                        and graph[ny][nx] == 0
                    ):
                        if (nx, ny) == (n - 1, m - 1):
                            return answer + 1
                        queue.append((nx, ny, True))
                        visited[ny][nx][True] = True
        answer += 1

    return -1
