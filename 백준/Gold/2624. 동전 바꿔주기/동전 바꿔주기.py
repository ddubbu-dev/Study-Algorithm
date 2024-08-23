import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리
target_money = int(readline())
T = int(readline())
coins = []  # (money, cnt)
for _ in range(T):
    coin, cnt = map(int, readline().split())
    coins.append((coin, cnt))


# 2. tabulation
dp = [0] * (target_money + 1)
dp[0] = 1  # 의미상 1

for coin, cnt in coins:  # Q. 반복문 순서가 아래로 가면 tabulation 안됨
    for money in range(target_money, 0, -1):  # Q. 왜 target_money > 1원 역순으로?
        for times in range(1, cnt + 1):
            # 코인 포함되어있다는 가정하에 하위 문제들의
            remain_money = money - coin * times
            if remain_money >= 0:  # 누적합
                dp[money] += dp[remain_money]
            else: # 시간초과; 더 이상 진행 불필요
                break
print(dp[target_money])