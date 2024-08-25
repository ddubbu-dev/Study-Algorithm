import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 전처리
N, target_money = map(int, readline().split())
coins = []
for _ in range(N):
    coins.append(int(readline()))


# 그리디 알고리즘
cnt = 0

# 정렬하는 속도도 줄이기 위해 뒤에서부터 순회

for i in range(len(coins) - 1, -1, -1):
    coin = coins[i]
    q = target_money // coin
    cnt += q
    target_money -= q * coin

    if target_money == 0:
        break

print(cnt)