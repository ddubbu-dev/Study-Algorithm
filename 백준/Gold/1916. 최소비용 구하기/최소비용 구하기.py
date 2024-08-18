"""
[고민되는 점]
Q. visited가 불필요할까?
- 현재 노드에서 costs 가 없데이트되지 않는다면, 더 가볼 필요 없으니 진행 안함.
- 혹 업데이트 된다면, 그 다음 진행을 위해 queue.append(item)

Q. costs= inf or 0 무엇으로 초기화 해야할까?
- inf 가 맞음, 시작점을 0으로 세팅해주면 inf 비교 후 0 할당 불필요해짐

[액션 정리]
0. 출발점 큐에 넣기
(아래는 while queue)
1. leftpop
2. 인접 노드 최소 비용 업데이트 (start_cost + edge_cost vs end_cost)
3. 만약 비용 업데이트 한다면, queue.append(item)

"""

from collections import deque
import sys
readline = lambda: sys.stdin.readline().strip()
# readline = input

N = int(readline())
M = int(readline())

GRAPH_SIZE = N + 1
graph = [[] for _ in range(GRAPH_SIZE)]


for _ in range(M):
    start, end, cost = map(int, readline().split())
    graph[start].append((end, cost))

target_s, target_e = map(int, readline().split())


def print_graph():
    for line in graph:
        print(line)


# print("===== (시작) graph edge 모음 =====")
# print_graph()
# print("===== (끝) graph edge 모음 =====")

costs = [float("inf")] * GRAPH_SIZE  # target_s ~ 각 index 까지의 비용

que = deque([target_s])
costs[target_s] = 0


def bfs():
    while que:
        start = que.popleft()
        for idx in range(len(graph[start])):
            edge_info = graph[start][idx]
            end = edge_info[0]

            if end == target_s:  # 출발지는 제외
                continue

            prev_cost = costs[end]  # 현재까지의 target_s ~ end 비용

            start_to_end_cost = edge_info[1]
            tmp = costs[start]
            new_cost = tmp + start_to_end_cost

            if costs[end] > new_cost:
                costs[end] = new_cost
                if not end in que:
                    que.append(end)


bfs()
print(costs[target_e])
