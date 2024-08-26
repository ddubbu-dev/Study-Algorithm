"""
[공간 최적화]
1D로 배낭문제 풀기
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 전처리
N, TARGET_WEIGHT = map(int, readline().split())
bag = []
for _ in range(N):
    w, v = map(int, readline().split())
    bag.append((w, v))

# dp[w] = w 무게에서 최대 가치
dp = [0] * (TARGET_WEIGHT + 1)

WEIGHT = 0
VALUE = 1

for i in range(N):
    for w in range(TARGET_WEIGHT, -1, -1):
        cur_weight = bag[i][WEIGHT]
        cur_value = bag[i][VALUE]
        if w - cur_weight >= 0:  # 유효한 인덱스 체크
            dp[w] = max(dp[w], dp[w - cur_weight] + cur_value)

print(dp[TARGET_WEIGHT])
