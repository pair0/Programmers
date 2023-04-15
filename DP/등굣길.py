def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                   # 위에서 오는 경우와 왼쪽에서 오는 경우를 더해줌
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]
