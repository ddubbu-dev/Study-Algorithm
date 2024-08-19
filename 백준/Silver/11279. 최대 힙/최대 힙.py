import sys

sys.setrecursionlimit(10**6)  # TODO: 아직 의미 이해를 못함
readline = lambda: sys.stdin.readline().strip()
# readline = input

from heapq import heapify, heappop, heappush

N = int(readline())
heap = []

for _ in range(N):
    num = int(readline())

    if num == 0:
        try:
            reversed_val = heappop(heap)
            print(-reversed_val)
        except:
            print(0)
    else:
        # 마이너스 연산 이유? 최소힙을 최대힙으로 만들기 위해
        heappush(heap, -num)
