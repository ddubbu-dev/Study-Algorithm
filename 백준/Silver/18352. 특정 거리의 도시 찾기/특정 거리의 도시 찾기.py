"""
[단계별로 푸는걸 추천]

- 난이도 하 #18352
- (v) 난이도 중 #1916
"""


from collections import deque

import sys
readline = lambda: sys.stdin.readline().strip()
#readline = input

N, M, K, X = map(int, readline().split())
GRAPH_SIZE = N + 1
graph = [[] for _ in range(GRAPH_SIZE)]

for _ in range(M):
    A, B = map(int, readline().split())
    graph[A].append(B)


que = deque([X])
min_distances = [float("inf")] * GRAPH_SIZE
min_distances[X] = 0  # 시작점 초기화

while que:
    start = que.popleft()
    for next in graph[start]:
        if min_distances[next] > min_distances[start] + 1:
            min_distances[next] = min_distances[start] + 1
            que.append(next)


cnt = 0
for node_idx in range(len(min_distances)):
    dist = min_distances[node_idx]
    if dist == K:
        print(node_idx)
        cnt += 1

if cnt == 0:
    print(-1)
