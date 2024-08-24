import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 1. 전처리
N = int(readline())
arr = list(map(int, readline().split()))

dp = [1] * N  # 자기 자신 유일 수열 미리 1 세팅


for idx in range(1, N):
    target = arr[idx]

    for j in range(idx):
        if target > arr[j]:
            dp[idx] = max(dp[idx], dp[j] + 1)


print(max(dp))
