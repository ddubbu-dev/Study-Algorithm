"""
[최대속도 이해 자료](https://soo-note.tistory.com/57)
[코드 이해 자료](https://velog.io/@grace0st/%EC%A0%90%ED%94%84-%EB%B0%B1%EC%A4%80-2253%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리

N, M = map(int, readline().split())
small = [int(readline()) for _ in range(M)]

max_speed = int(2 * N ** (1 / 2)) + 1  # 단순히 N까지 증가하겠지라고 생각했는데

# dp[v][i] = v속도로 i번째 돌에 도착한 최소 점프 횟수
dp = [[float("inf")] * (max_speed + 1) for _ in range(N + 1)]
dp[1][0] = 0

for i in range(2, N + 1):
    if i in small:
        continue
    for v in range(1, int((2 * i) ** 0.5) + 1):
        prev_in_가속 = dp[i - v][v - 1]
        prev_in_정속 = dp[i - v][v]
        prev_in_감속 = dp[i - v][v + 1]
        dp[i][v] = min(prev_in_가속, prev_in_정속, prev_in_감속) + 1


ans = min(dp[N])
if ans == float("inf"):
    print(-1)
else:
    print(ans)
