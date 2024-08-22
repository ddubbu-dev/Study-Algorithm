import sys

sys.setrecursionlimit(10**6)
readline = lambda: sys.stdin.readline().strip()

N = int(readline())

is_updated = False
min_cost = float("inf")
for _ in range(N):
    to_door, bread_arrive = map(int, readline().split())

    if to_door <= bread_arrive:
        min_cost = min(min_cost, bread_arrive)
        is_updated = True

if is_updated:
    print(min_cost)
else:
    print(-1)