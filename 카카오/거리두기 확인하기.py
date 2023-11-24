# 대기실 5개, 각 대기실은 5x5
# 맨해튼 거리 |r1-r2|+|c1-c2| 2이하로 앉기 X
# 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우 혀용
from collections import deque


def bfs(graph, x, y, visited):
    # 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque([(x, y)])
    visited2 = [[False] * 5 for _ in range(5)]
    visited2[y][x] = True
    x1, y1 = x, y

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < 5
                and 0 <= ny < 5
                and graph[ny][nx] != "X"
                and not visited[ny][nx]
                and not visited2[ny][nx]
            ):
                queue.append((nx, ny))
                visited[ny][nx] = True
                if graph[ny][nx] == "P":
                    if abs(x1 - nx) + abs(y1 - ny) <= 2:
                        if x1 == nx:
                            flagx = 0
                            for p in range(y1 + 1, ny):
                                if "X" in graph[p][nx]:
                                    flagx = 1
                                    break
                            if flagx == 1:
                                continue
                        elif y1 == ny:
                            if "X" in graph[ny][x1 + 1 : nx]:
                                continue
                        else:
                            if x1 > nx:
                                if (
                                    graph[y1][x1 - 1] == "X"
                                    and graph[y1 + 1][x1] == "X"
                                ):
                                    continue
                            else:
                                if (
                                    graph[y1 + 1][x1] == "X"
                                    and graph[y1][x1 + 1] == "X"
                                ):
                                    continue
                        return 0  # 맨해튼 거리 안지킴

    return 1  # 맨해튼 거리 지킴


def solution(places):
    answer = []
    for i in range(5):
        visited = [[False] * 5 for _ in range(5)]
        flag = -1
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    visited[j][k] = True
                    flag = bfs(places[i], k, j, visited)
                if flag == 0:
                    break
            if flag == 0:
                break
        if flag == -1:
            flag = 1
        answer.append(flag)

    return answer
