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
# Q. visited 필요할까? 아니면 모든 노드를 돌아다닐까?????

que = deque([target_s])


def bfs():
    while que:
        start = que.popleft()
        for idx in range(len(graph[start])):
            edge_info = graph[start][idx]
            end = edge_info[0]

            if end == target_s:  # 출발지는 제외
                continue

            # 아이디어1) 아니면 업데이트할 때 넣어줄까?
            prev_cost = costs[end]  # 현재까지의 target_s ~ end 비용

            start_to_end_cost = edge_info[1]
            tmp = costs[start] if costs[start] != float("inf") else 0  # TODO 아리까리
            new_cost = tmp + start_to_end_cost

            # print(f"edge_info={edge_info}, prev_cost={prev_cost}, new_cost={new_cost}")

            if prev_cost <= new_cost:  # 의심) visited가 여기서 관리되지 않을까?
                # TODO: 같을경우 제외해줌 - 다시 돌려보기
                continue
            else:
                costs[end] = new_cost
                if not end in que:  # 아이디어2) que에 두번 들어가서?
                    que.append(end)


bfs()

print(costs[target_e])