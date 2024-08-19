"""
Q1. 이전 시간초과 코드에서 graph에 tuple을 관리하지 않고, que에 days를 함께 관리했더니
왜 시간초과가 발생하지 않는걸까.. 이건 GPT가 잡아준거라 풀었다고는 못하겠다...

Q2. 그리고 익은 경우 다른 곳에서 퍼진걸로 더 빨리 익을 수도 있잖아 NO_RIPEN만 비교하는걸까?
"""

from collections import deque

import sys
input = lambda: sys.stdin.readline()

M, N, H = map(int, input().split())
graph = []  # 3D 배열

# 상태 상수 정의
RIPEN_TOMATO = 1
NO_RIPEN_TOMATO = 0
NO_EXIST_TOMATO = -1

# 큐 초기화
que = deque()

# 그래프 입력 및 초기화
for height in range(H):
    board = []
    for column in range(N):
        line = list(map(int, input().split()))
        board.append(line)
        for row in range(M):
            if line[row] == RIPEN_TOMATO:
                que.append((row, column, height, 0)) #마지막 요소 소요 날짜 
    graph.append(board)

# 모든 토마토가 익었는지 체크
if not que:
    print(-1)
    exit()


directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

max_days = 0

while que:
    x, y, z, days = que.popleft()

    for dx, dy, dz in directions:
        new_x = x + dx
        new_y = y + dy
        new_z = z + dz

        if 0 <= new_x < M and 0 <= new_y < N and 0 <= new_z < H:
            if graph[new_z][new_y][new_x] == NO_RIPEN_TOMATO:
                graph[new_z][new_y][new_x] = RIPEN_TOMATO 
                que.append((new_x, new_y, new_z, days + 1))
                max_days = max(max_days, days + 1)  # 최대 날짜 업데이트

# 모든 토마토가 익었는지 확인
for height in range(H):
    for column in range(N):
        for row in range(M):
            if graph[height][column][row] == NO_RIPEN_TOMATO:
                print(-1)
                exit()

print(max_days)
