"""
5kg greedy > 최적해 아니면
5kg--, 3kg++ 하나씩 늘려가보기

[반례](https://www.acmicpc.net/board/view/143009)
- 5의배수 처리
"""

import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 1. 전처리
target = int(readline())
raw_target = target
FIVES = 5
THREE = 3

cnt = 0

q = target // FIVES
target -= FIVES * q
cnt += q

while target > 0:
    q = target // THREE
    if target - q * THREE == 0:
        cnt += q
        break

    target += FIVES
    cnt -= 1
    if target > raw_target:
        cnt = -1
        break

print(cnt)
