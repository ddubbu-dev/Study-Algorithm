"""
[풀이]
- [left(max_heap)][right(min_heap)]
- len(left) = len(rihgt) 혹은 len(right) + 1
- 위 조건을 통해 left.heappop 으로 쉽게 mid 값 구할 수 있음 
- 계속 크기 조정 필요함
"""
import sys
readline = lambda: sys.stdin.readline().strip()
# readline = input

import heapq

left = []  # max힙 (- 반전 주의)
right = []  # min힙

N = int(readline())

for _ in range(N):
    num = int(readline())

    if len(left) == 0:
        heapq.heappush(left, -num)
    else:
        left_max = left[0]
        right_min = right[0] if len(right) > 0 else float("inf")

        if num <= right_min:
            heapq.heappush(left, -num)
            if len(left) >= len(right) + 2:
                heapq.heappush(right, -heapq.heappop(left))
        else:
            heapq.heappush(right, num)
            if len(right) >= len(left) + 1:
                heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])
