### 시간 초과
import sys 
sys.setrecursionlimit(100000)

### 하좌우상 표시 (d, l, r, u)
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
directions = 'dlru'

def dfs(graph, n, m, x, y, r, c, k):
    if (x, y) == (r, c) and graph[x][y] == k:
        return ''
    elif graph[x][y] > k:
        return "impossible"
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if 0 < nx <= n and 0 < ny <= m:
            temp = graph[nx][ny]
            graph[nx][ny] = graph[x][y] + 1
            answer = dfs(graph, n, m, nx, ny, r, c, k)
            if answer != "impossible":
                return directions[i] + answer
            graph[nx][ny] = temp
            
    return "impossible"
    
def solution(n, m, x, y, r, c, k):
    graph = [[0] * (m+1) for _ in range(n+1)]
    answer = dfs(graph, n, m, x, y, r, c, k)
    
    return answer

###정답
def calc_dist(x, y, r, c):
    return abs(x - r) + abs(y - c)

def solution(n, m, x, y, r, c, k):
    if (k - calc_dist(x, y, r, c)) % 2 or k < calc_dist(x, y, r, c):
        return "impossible"
    answer = ""
    move = 0
    # 아래로 최대한 이동
    while x < n and (k - move) > calc_dist(x, y, r, c):
        move += 1
        x += 1
        answer += "d"
    # 좌측으로 최대한 이동
    while 1 < y and (k - move) > calc_dist(x, y, r, c):
        move += 1
        y -= 1
        answer += "l"
        
    # 우좌 반복 이동
    while (k - move) > calc_dist(x, y, r, c):
        move += 2
        answer += "rl"
    
    # 가야할 길로 이동 dlru 순으로 이동
    if x < r:
        answer += "d" * (r - x)
        x = r
    if y > c:
        answer += "l" * (y - c)
        y = c
    if y < c:
        answer += "r" * (c - y)
        y = c
    if x > r:
        answer += "u" * (x - r)
        x = r
    return answer
