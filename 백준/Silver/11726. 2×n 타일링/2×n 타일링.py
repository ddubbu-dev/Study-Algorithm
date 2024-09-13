"""
d[i] = d[i-1] + d[i-2]
"""

import sys

readline = lambda: sys.stdin.readline().strip()
#readline = input

MOD = 10007

n = int(readline())
SIZE = n + 1
dp = [0] * SIZE
dp[0] = 1
dp[1] = 1

for i in range(2, SIZE):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n]%MOD)
