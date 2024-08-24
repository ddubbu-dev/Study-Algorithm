"""
[참고자료](https://claude-u.tistory.com/208)
"""

import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 1. 전처리

N, K = map(int, readline().split())
bag = [(0, 0)]  # empty item


for _ in range(N):
    w, v = map(int, readline().split())
    bag.append((w, v))

WEIGHT = 0
VALUE = 1

# dp[i][w] = i번째 물건까지 사용해서 w무게를 갖는 최대 가치
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, K + 1):
        cur_weight = bag[i][WEIGHT]
        cur_value = bag[i][VALUE]

        if w >= cur_weight:  # 과거값으로부터 갱신 가능
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cur_weight] + cur_value)
        else:  # 과거값 그대로 갱신
            dp[i][w] = dp[i - 1][w]

print(dp[N][K])
