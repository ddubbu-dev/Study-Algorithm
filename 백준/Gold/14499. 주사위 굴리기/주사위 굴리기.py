"""
[ref](https://hongcoding.tistory.com/128)
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, x, y, K = map(int, input().split())
board = []
dice = [0] * 6
upper_idx = 0  # 윗면
bottom_idx = 5  # 아랫면 idx

for _ in range(n):
    nums = list(map(int, input().split()))
    board.append(nums)

cmds = list(map(lambda s: int(s) - 1, input().split()))


def turn(cmd):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if cmd == 0:
        dice = [d, b, a, f, e, c]
    elif cmd == 1:
        dice = [c, b, f, a, e, d]
    elif cmd == 2:
        dice = [e, a, c, d, f, b]
    else:
        dice = [b, f, c, d, a, e]


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for cmd in cmds:
    x += dx[cmd]
    y += dy[cmd]

    if x < 0 or x >= n or y < 0 or y >= m:  # out of range
        x -= dx[cmd]
        y -= dy[cmd]
        continue

    turn(cmd)

    if board[x][y] == 0:
        board[x][y] = dice[bottom_idx]
    else:
        dice[bottom_idx] = board[x][y]
        board[x][y] = 0

    print(dice[0])
