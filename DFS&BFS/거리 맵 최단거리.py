from collections import deque


def solution(maps):
    answer = 0

    # 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque([(0, 0)])
    M = len(maps) - 1
    N = len(maps[0]) - 1

    while queue:
        x, y = queue.popleft()

        if x == N and y == M:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 넘어가면 안됨
            if nx < 0 or ny < 0 or nx > N or ny > M:
                continue

            # 벽을 만나면 안됨
            if maps[ny][nx] == 0:
                continue

            # 벽이 아니므로 진행
            if maps[ny][nx] == 1:
                # 이동한 횟수 세기
                maps[ny][nx] = maps[y][x] + 1
                queue.append((nx, ny))

    if maps[M][N] != 1:
        answer = maps[M][N]
    else:
        answer = -1

    return answer


# 100점 짜리
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    count = 1

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == n-1 and y == m-1:
                return count
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        count += 1

    return -1
