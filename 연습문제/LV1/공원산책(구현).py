def solution(park, routes):
    answer = []
    start_x, start_y = 0, 0

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                start_x, start_y = j, i

    for i in routes:
        flag = -1
        if i[0] == 'N':
            # 벽을 만나면 안됨
            if start_y - int(i[2]) < 0:
                flag = 0
            # 장애물을 만나면 안됨
            else:
                for j in range(start_y-int(i[2]), start_y):
                    if park[j][start_x] == "X":
                        flag = 0
                        break
            if flag != 0:
                start_y -= int(i[2])
        elif i[0] == 'S':
            # 벽을 만나면 안됨
            if start_y + int(i[2]) > len(park)-1:
                flag = 0
            # 장애물을 만나면 안됨
            else:
                for j in range(start_y+1, start_y+int(i[2])+1):
                    if park[j][start_x] == "X":
                        flag = 0
                        break
            if flag != 0:
                start_y += int(i[2])
        elif i[0] == 'W':
            # 벽을 만나면 안됨
            if start_x - int(i[2]) < 0:
                flag = 0
            # 장애물을 만나면 안됨
            else:
                for j in range(start_x-int(i[2]), start_x):
                    if park[start_y][j] == "X":
                        flag = 0
                        break
            if flag != 0:
                start_x -= int(i[2])
        elif i[0] == 'E':
            # 벽을 만나면 안됨
            if start_x + int(i[2]) > len(park[start_y])-1:
                flag = 0
            # 장애물을 만나면 안됨
            else:
                for j in range(start_x+1, start_x+int(i[2])+1):
                    if park[start_y][j] == "X":
                        flag = 0
                        break
            if flag != 0:
                start_x += int(i[2])

    answer = [start_y, start_x]
    return answer
