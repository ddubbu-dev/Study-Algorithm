"""
[출처](https://e-juhee.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-2617-%EA%B5%AC%EC%8A%AC%EC%B0%BE%EA%B8%B0-DSF)
- 어떻게 dfs 아이디어를 떠올릴 수 있을까?
"""

import sys

sys.setrecursionlimit(10**6)
readline = input  # lambda: sys.stdin.readline().strip()

N, M = map(int, readline().split())
GRAPH_SIZE = N + 1
heavy_list = [[] for _ in range(GRAPH_SIZE)]
light_list = [[] for _ in range(GRAPH_SIZE)]

for _ in range(M):
    heavy, light = map(int, readline().split())
    heavy_list[heavy].append(light)
    light_list[light].append(heavy)


def dfs(list, root):
    cnt = 0
    for node in list[root]:
        if not visited[node]:
            visited[node] = True
            cnt += 1
            cnt += dfs(list, node)
    return cnt


mid = (GRAPH_SIZE) / 2
cant_mid_cnt = 0

for root in range(1, GRAPH_SIZE):
    visited = [False] * GRAPH_SIZE

    if dfs(heavy_list, root) >= mid:
        cant_mid_cnt += 1
    if dfs(light_list, root) >= mid:
        cant_mid_cnt += 1


print(cant_mid_cnt)
