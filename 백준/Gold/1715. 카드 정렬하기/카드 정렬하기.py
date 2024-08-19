"""
Q. 이게 왜 우선순위큐임???? 응??
A. 연산수를 줄이려면,
- 매 연산 시 이전 누적값 vs 최솟값을 더해서 점차 누적합을 늘려가야함
- 이때 min 으로 진행하면, N! 연산 횟수가 필요함.
- 힙을 이용하면 logN 으로 횟수가 줄겠지?
"""
import sys

sys.setrecursionlimit(10**6)  # TODO: 아직 의미 이해를 못함
readline = lambda: sys.stdin.readline().strip()
# readline = input

from heapq import heappop, heappush

N = int(readline())
heap = []

for _ in range(N):
    num = int(readline())
    heappush(heap, num)

if len(heap) == 1:
    print(0)  # 이미 정렬됨
    exit()

acc = 0
while len(heap) >= 2:
    A = heappop(heap)
    B = heappop(heap)

    result = A + B
    acc += result

    heappush(heap, result)

print(acc)
