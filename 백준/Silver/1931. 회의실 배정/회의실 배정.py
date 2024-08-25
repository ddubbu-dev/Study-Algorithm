"""
[반례]
- 끝점이 같은경우 가능한거 먼저하고
- 시작점 끝점이 같은 경우 바로 cnt++

3
2 3
2 2
1 2

ans: 3
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 전처리
N = int(readline())
meets = []
for _ in range(N):
    s, e = map(int, readline().split())
    meets.append((s, e))

# 그리디 알고리즘 (정렬 기반)
meets.sort(key=lambda x: (x[1], x[0]))

cnt = 0

last_end = -1
for s, e in meets:
    if last_end <= s:
        cnt += 1
        last_end = e

print(cnt)
