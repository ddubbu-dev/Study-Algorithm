
from collections import deque

import sys
readline = lambda: sys.stdin.readline().strip()
# readline = input

que = deque()

T = int(readline())

for i in range(T):
    cmds = readline().split()

    if cmds[0] == "push":
        que.append(cmds[1])
    elif cmds[0] == "pop":
        try:
            print(que.popleft())
        except:
            print(-1)
    elif cmds[0] == "size":
        print(len(que))
    elif cmds[0] == "empty":
        print(int(len(que) <= 0))
    elif cmds[0] == "front":
        try:
            print(que[0])
        except:
            print(-1)
    elif cmds[0] == "back":
        try:
            print(que[-1])
        except:
            print(-1)
