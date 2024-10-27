"""
binary search
- target: 상한액 찾기
- condition: 총 예산 이하
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

_ = int(input())
nums = list(map(int, input().split()))
budget = int(input())

l = 0
r = max(nums)

best_limit = 0

while l <= r:
    limit = (l + r) // 2
    tmp = sum(list(map(lambda n: min(n, limit), nums)))

    if tmp > budget:
        r = limit - 1
    else:
        best_limit = max(limit, best_limit)
        l = limit + 1

print(best_limit)
