"""
순서 보장 필요
0 => 1 => 2 => 0 ...
"""

import sys

readline = lambda: sys.stdin.readline().strip()

# 전처리
n = int(readline())
data = list(map(int, readline().split()))

cnt = 0
last_milk = 2
for milk in data:
    if last_milk == 2 and milk == 0:
        cnt += 1
        last_milk = milk
    elif last_milk == 0 and milk == 1:
        cnt += 1
        last_milk = milk
    elif last_milk == 1 and milk == 2:
        cnt += 1
        last_milk = milk

print(cnt)