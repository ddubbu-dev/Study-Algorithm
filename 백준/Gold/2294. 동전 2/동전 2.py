import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리
n, target_money = map(int, readline().split())
coins = []
for _ in range(n):
    coins.append(int(readline()))

# 2. dp[i]: i원을 만들 때 필요한 동전 최소 개수

dp = [float("inf")] * (target_money + 1)
dp[0] = 0


for coin in coins:
    for money in range(coin, target_money + 1):
        dp[money] = min(dp[money], dp[money - coin] + 1)

if dp[money] == float("inf"):
    print(-1)
else:
    print(dp[target_money])