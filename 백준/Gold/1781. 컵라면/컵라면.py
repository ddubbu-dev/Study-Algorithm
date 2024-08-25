
## 심플버전
# [참고 풀이](https://thought-process-ing.tistory.com/204)

import sys

readline = lambda: sys.stdin.readline().strip()

# 전처리
n = int(readline())
table = []
for _ in range(n):
    d, c = map(int, readline().split())
    table.append((d, c))
table.sort()

# 순회
import heapq

hq = []

for i in table:
    heapq.heappush(hq, i[1])
    if i[0] < len(hq):
        heapq.heappop(hq)

print(sum(hq))
