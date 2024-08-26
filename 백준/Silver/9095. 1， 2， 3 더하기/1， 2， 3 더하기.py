"""
- Bottom-Up
- [참고자료](https://great-park.tistory.com/127)
"""

import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 1. 전처리
T = int(readline())
coins = [1, 2, 3]

MAX_TARGET = 10
# dp[i] = i 수를 만들 수 있는 가짓수
dp = [0] * (MAX_TARGET + 1)
# basis
dp[0] = 1  # 의미상; 아무것도 선택안함 가짓수
dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4, MAX_TARGET + 1):
    # 누적합
    for coin in coins:
        dp[i] += dp[i - coin]


for _ in range(T):
    N = int(readline())
    print(dp[N])