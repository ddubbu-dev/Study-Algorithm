"""
[반례](https://www.acmicpc.net/board/view/4421)
- dp 중 최대값을 출력해야함
- prev dp 중에 보다 큰 nums[i] 값이면서 best 값으로부터 갱신해야함
-- 가장 최근 prev_i 가 베스트값일거란 보장이 없음
-- Q. 그럼 N^2 위험은 없는지? 최대 O(N^2=10^6)
"""

import sys
readline = lambda: sys.stdin.readline().strip()

# 1. 전처리
N = int(readline())
nums = [0] + list(map(int, readline().split()))

# dp[i] = i번째 요소를 포함해, 가장 긴 감소하는 부분 수열 길이
dp = [1] * (N + 1)  # init
dp[0] = 0

for i in range(2, N + 1):
    max_len = 0
    for j in range(1, i):
        if nums[j] > nums[i]:
            max_len = max(max_len, dp[j])
    dp[i] = max_len + 1

print(max(dp))