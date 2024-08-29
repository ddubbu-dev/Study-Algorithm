"""
[시간] 10:15 ~ 10:30
[문제 분석]
- 숫자별 최대 사용 횟수 정해져 있음
"""


import sys

sys.setrecursionlimit(10**6)
readline = lambda: sys.stdin.readline().strip()

N = int(readline())
nums = list(map(int, readline().split()))
max_cnt = int(readline())

# 코인 #유한개 #동전수

# dp[i] = 숫자 i를 만들기 위해 필요한 최소 동전 개수
MAX_TARGET = 1000 * 50
dp = [sys.maxsize] * (MAX_TARGET + 1)

# 초기화
dp[0] = 0
dp[1] = 1


for num in nums:
    for target_num in range(1, MAX_TARGET + 1):
        if target_num - num >= 0:
            dp[target_num] = min(dp[target_num], dp[target_num - num * 1] + 1)

for num, cnt in enumerate(dp):
    if cnt > max_cnt:
        winner_num = num
        if winner_num % 2 == 0:
            print(f"holsoon win at {winner_num}")
        else:
            print(f"jjaksoon win at {winner_num}")
        exit()
