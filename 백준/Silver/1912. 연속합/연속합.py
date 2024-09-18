"""
[시도3] 초기값 0말고 -Inf

[시도2] dp[n] 차원수 줄이기

[시도1] sub problem, dp[n][n]
[실패] 메모리초과
공간복잡도(n^2=10^10) 약 (10^4)MB > 128MB
"""

import sys
readline = lambda: sys.stdin.readline().strip()

# 전처리
n = int(readline())
SIZE = n  # idx=0 부터 시작해도 됨
nums = list(map(int, readline().split()))

# dp[i] : 범위(0~i) nums[i] 연속합 최댓값
dp = [-sys.maxsize] * SIZE
dp[0] = nums[0]

# dp 채우기
for i in range(1, SIZE):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])  # 연속으로 붙일지 말지

print(max(dp))