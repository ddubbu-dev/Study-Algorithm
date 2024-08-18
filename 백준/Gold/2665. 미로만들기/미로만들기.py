"""
[아이디어1]
- 일반적으로 시작 > 끝 경로를 찾아가는 BFS
- 하지만, 끝방까지 도달하지 못하면? 검은방도 갈 수 있는 케이스,,
- 가장 최소로 벽을 깨면서 이동하려면?
-- 흰색있으면, 무조건 그쪽으로..
-- 만약, 검은색 벽 한개만 깨면 되는거면?
-- 벽을 깰 때는 y++, x++ 방향으로만

[아이디어2]
- ALL 흰색길로만 BEST sol
- (N,N) 가장 가깝게 BFS로 이동 => 그리고 분할탐색? 작은 범위에서?

[아이디어3](https://velog.io/@whddn0221/%EB%B0%B1%EC%A4%80-2665-%EB%AF%B8%EB%A1%9C%EB%A7%8C%EB%93%A4%EA%B8%B0-BFS-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90)
1. 흰색길 >> 검은색길
2. 흰색길로 다 갔는데 못갔다? 그럼 검은색길로 뚫어서 진행해야함.
- (x) 이때 검은색은 y++, x++ 방향으로만? 아냐, 왼쪽을 1개만 뚫리면 될 수 도 있어
- 흰색queue, 검은색queue 따로 둬야하나??
-- 왜냐하면, 흰색 우선순위가 높아서 지난 노드에서 넣어둔 검은색돌보다 앞쪽에 넣어져야해서
-- 노래방 우선예약처럼 말이지

[궁금한점]
- visited 관리를 input이랑 관리할때, 아닐때는 언제인가?

"""


from collections import deque

import sys
readline = lambda: sys.stdin.readline().strip()
readline = input


near_cases = [(1, 0), (-1, 0), (0, 1), (0, -1)]
WHITE_ROOM = 1
BLACK_ROOM = 0

N = int(readline())
rooms = []
visited_graph = []


for _ in range(N):
    line = list(map(int, list(readline())))
    rooms.append(line)
    visited_graph.append([(0, 0)] * N)  # [steps, break_black_rooms]


def print_graph(graph):
    for line in graph:
        print(line)


# print_graph(rooms)


visited_graph[0][0] = (1, 0)  # 시작점
white_queue = deque([(0, 0)])
black_queue = deque()


def bfs():
    while white_queue or (len(white_queue) == 0 and black_queue):

        # print(f"white_queue={white_queue}")
        # print(f"black_queue={black_queue}")

        if white_queue:
            x, y = white_queue.popleft()
        elif black_queue:
            x, y = black_queue.popleft()

        if x == N - 1 and y == N - 1:
            break

        for dx, dy in near_cases:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < N and 0 <= new_y < N:
                prev_steps = visited_graph[x][y][0]
                prev_break_rooms = visited_graph[x][y][1]
                # print(f"prev_steps={prev_steps}, prev_break_rooms={prev_break_rooms}")
                if not visited_graph[new_x][new_y][0]:
                    if rooms[new_x][new_y] == WHITE_ROOM:
                        white_queue.append((new_x, new_y))
                        visited_graph[new_x][new_y] = (prev_steps + 1, prev_break_rooms)

                    else:  # BLACK_ROOM
                        black_queue.append((new_x, new_y))
                        visited_graph[new_x][new_y] = (
                            prev_steps + 1,
                            prev_break_rooms + 1,
                        )


bfs()
break_black_rooms = visited_graph[N - 1][N - 1][1]
print(break_black_rooms)