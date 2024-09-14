"""
[풀이]
- cnt table 작성
- sort (nlogn = 10^5*5 < 1초)
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input
N = int(readline())
cnt_table = {}

for i in range(N):
    num = int(readline())
    prev = cnt_table.get(num, 0)

    cnt_table[num] = prev + 1


result = 2**62  # inf
max_cnt = 0
for num, cnt in cnt_table.items():
    if (cnt > max_cnt) or (cnt == max_cnt and num < result):
        max_cnt = cnt
        result = num


print(result)