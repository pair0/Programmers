# y=n, x=m
from collections import deque


def bfs(land, x, y, visited, m, n, setdp):
    queue = deque([(x, y)])
    visited[y][x] = True
    count = 1
    setdp.add(x)

    # 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < m
                and 0 <= ny < n
                and visited[ny][nx] == False
                and land[ny][nx] == 1
            ):
                queue.append((nx, ny))
                setdp.add(nx)
                visited[ny][nx] = True
                count += 1
    return count


def solution(land):
    land_x = len(land[0])
    land_y = len(land)
    dp = [0] * land_x
    visited = [[False] * land_x for _ in range(land_y)]

    for i in range(land_x):
        answer = 0
        for j in range(land_y):
            if land[j][i] == 1 and visited[j][i] == False:
                setdp = set()
                answer = bfs(land, i, j, visited, land_x, land_y, setdp)
                for i in list(setdp):
                    dp[i] += answer

    return max(dp)
