"""
- 유레카!!
front(앞), rear(꼬리); 말 그대로 queue는 스프링통 뿐만 아니라 뱀이라고 볼수도 있다니
- 주의
-- 1) 벽 뿐만 아니라, 자기 몸통 만나도 아웃
-- 2) 먹은 사과는 치워야함
-- 3) 마지막 질주에서도 자기 몸통 만날 수 있음
-- 4) python 리스트는 음수 인덱싱 가능함 (크기 초과만 에러난다 ㅠㅠ)
"""

from collections import deque

# import sys
# readline = lambda: sys.stdin.readline().strip()

readline = input

N = int(readline())

# apple map
K = int(readline())
apples = []
for _ in range(N + 1):  # 1 ~ N 범위로 만들어주기
    arr = [False] * (N + 1)
    apples.append(arr)


for i in range(K):
    x, y = map(int, readline().split())
    apples[x][y] = True


# 뱀 움직임
que = deque([(1, 1)])
cmd_num = int(readline())

x, y = 1, 1

position_idx = 0  # first, right
positions = ["right", "down", "left", "up"]


total_tick = 0
for i in range(cmd_num):
    num, guide = readline().split()
    break_tick = int(num)

    # 명령대로 움직이기
    while total_tick < break_tick:
        # print(
        #     f"[total: {total_tick}s] que={que}, after={break_tick-total_tick}s, will be {guide}"
        # )

        position = positions[position_idx]

        if position == "right":
            y += 1
        elif position == "down":
            x += 1
        elif position == "left":
            y -= 1
        elif position == "up":
            x -= 1

        total_tick += 1

        if 1 <= x <= N and 1 <= y <= N:
            next_pos = (x, y)
            que.append(next_pos)

            if que.count(next_pos) >= 2:
                # print(f"[exit] que={que}")

                print(total_tick)
                exit()
        else:
            print(total_tick)
            exit()

        try:
            if apples[x][y]:
                apples[x][y] = False
                continue
            else:
                que.popleft()
        except:
            # print(f"[exit] que={que}")

            print(total_tick)
            exit()

    if guide == "D":
        position_idx = (position_idx + 1) % len(positions)
    elif guide == "L":
        position_idx = (position_idx - 1 + len(positions)) % len(positions)

position = positions[position_idx]


while 1 <= x <= N and 1 <= y <= N:
    # print(f"[total: {total_tick}s] que={que}")

    total_tick += 1

    if position == "right":
        y += 1
    elif position == "down":
        x += 1
    elif position == "left":
        y -= 1
    elif position == "up":
        x -= 1

    next_pos = (x, y)
    que.append(next_pos)
    if que.count(next_pos) >= 2:
        # print(f"[exit] que={que}")

        print(total_tick)
        exit()
    que.append(next_pos)

# print(f"[exit] que={que}")
print(total_tick)
