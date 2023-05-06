from collections import deque


def solution(board):
    answer = 0
    N = len(board)
    # 상하좌우 대각선 정의
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    visited = [[False] * N for _ in range(N)]

    def bfs(x, y):
        queue = deque([(x, y)])
        while queue:
            a, b = queue.popleft()
            visited[a][b] = True

            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b

                #
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        queue.append((nx, ny))
                    else:
                        board[nx][ny] = 2

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                bfs(i, j)

    for i in range(N):
        answer += board[i].count(0)
    return answer
