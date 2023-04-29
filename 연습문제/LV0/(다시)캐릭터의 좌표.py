def move(direction, x, y, dx, dy, max_x, max_y):
    temp_x = x + dx[direction]
    temp_y = y + dy[direction]

    if abs(temp_x) > abs(max_x) or abs(temp_y) > abs(max_y):
        return x, y
    else:
        return temp_x, temp_y


def solution(keyinput, board):
    answer = []

    # 맵 넓이
    max_x = board[0]//2
    max_y = board[1]//2

    # 현재 위치
    x = 0
    y = 0
    # 상하좌우 표시
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in keyinput:
        if i == "left":
            x, y = move(2, x, y, dx, dy, max_x, max_y)
        elif i == "right":
            x, y = move(3, x, y, dx, dy, max_x, max_y)
        elif i == "up":
            x, y = move(0, x, y, dx, dy, max_x, max_y)
        elif i == "down":
            x, y = move(1, x, y, dx, dy, max_x, max_y)

    answer = [x, y]
    return answer
