import sys
readline = lambda: sys.stdin.readline().strip()

rooms = int(readline())
actions = int(readline())
remain_rooms = list(range(1, rooms + 1))


for _ in range(actions):
    x, y = map(int, readline().split())

    for delete_room_num in range(x, y):  # y 제외
        if delete_room_num in remain_rooms:
            remain_rooms.remove(delete_room_num)


print(len(remain_rooms))
