"""
binary search
- target: (maximum) same length
- condition: K - cut -> N
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))


l = 1
r = max(lines)
best_len = 0  # max

while l <= r:
    len = (l + r) // 2
    cnt = 0
    for line in lines:
        q = line // len
        cnt += q

    if cnt >= N:  # 충분, 길이 늘리기
        best_len = max(best_len, len)

        l = len + 1
    else:
        r = len - 1

print(best_len)