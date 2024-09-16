"""
[아이디어]
- 오름차순 후 누적합 구하기?
"""

import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 전처리
n = int(readline())
A = list(map(int, readline().split()))
A.sort()

acc = [0]

for idx in range(n):
    acc.append(acc[-1] + A[idx])

print(sum(acc))
