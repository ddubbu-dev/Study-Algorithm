
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

DIRTY_ROOM = 0
CLEAN_ROOM = -1
WALL = 1
BACK = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 방향; 북/동/남/서
FRONT = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def turn(d: int) -> int:  # 반시계 방향 회전
    return (d + 3) % 4

cnt = 0

while True:
    if grid[x][y] == DIRTY_ROOM:
        cnt += 1
        grid[x][y] = CLEAN_ROOM

    has_dirty_room = False
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 가장자리
            continue

        if grid[nx][ny] == DIRTY_ROOM:
            has_dirty_room = True
            break

    if has_dirty_room:  # 조건3
        d = turn(d)
        dx, dy = FRONT[d]
        if (0 <= x + dx < n and 0 <= y + dy < m) and grid[x + dx][y + dy] == DIRTY_ROOM:
            x += dx
            y += dy
    else:  # 조건2
        dx, dy = BACK[d]
        if (0 <= x + dx < n and 0 <= y + dy < m) and grid[x + dx][y + dy] != WALL:  # 2-1
            x += dx
            y += dy
        else:  # 2-2
            break


print(cnt)
