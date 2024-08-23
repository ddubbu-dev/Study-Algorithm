import sys

readline = lambda: sys.stdin.readline().strip()
readline = input


T = int(readline())
for _ in range(T):
    # 1. 전처리
    N = int(readline())
    coins = list(map(int, readline().split()))  # 유한개의 동전
    target_money = int(readline())

    # 2. tabulation; dp[i] i원을 만들 수 있는 가짓수
    dp = [0] * (target_money + 1)
    dp[0] = 1

    for coin in coins:
        for money in range(target_money, 0, -1):
            cnt = money // coin
            for i in range(1, cnt + 1):
                remain_money = money - coin * i
                if remain_money >= 0:
                    dp[money] += dp[remain_money]

    print(dp[target_money])
