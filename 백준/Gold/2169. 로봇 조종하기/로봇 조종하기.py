"""
[참고자료](https://velog.io/@dosadola/python-%EB%A1%9C%EB%B4%87-%EC%A1%B0%EC%A2%85%ED%95%98%EA%B8%B0-%EB%B0%B1%EC%A4%80-2169)
"""

import sys
import copy

readline = lambda: sys.stdin.readline().strip()
readline = input

# 1. 전처리
N, M = map(int, readline().split())
# dp[i][j]= (i,j) 도착시 최대누적합
dp = []
for _ in range(N):
    dp.append(list(map(int, readline().split())))

# 2. dp 진행
# init (1번째행; 오른쪽 이동)
for col in range(1, M):
    dp[0][col] += dp[0][col - 1]

# 2번째행부터 계산
for row in range(1, N):
    left_to_right = copy.deepcopy(dp[row])
    for col in range(M):  # 왼쪽 끝에서부터 >>
        if col == 0:  # only 아래로 이동
            left_to_right[col] += dp[row - 1][col]
        else:
            from_top, from_left = dp[row - 1][col], left_to_right[col - 1]
            left_to_right[col] += max(from_top, from_left)

    right_to_left = copy.deepcopy(dp[row])
    for col in range(M - 1, -1, -1):  # << 오른쪽 끝에서부터
        if col == M - 1:  # only 아래로 이동
            right_to_left[col] += dp[row - 1][col]
        else:
            from_top, from_right = dp[row - 1][col], right_to_left[col + 1]
            right_to_left[col] += max(from_top, from_right)

    max_result = [max(left_to_right[i], right_to_left[i]) for i in range(M)]
    dp[row] = copy.deepcopy(max_result)


print(dp[N - 1][M - 1])
