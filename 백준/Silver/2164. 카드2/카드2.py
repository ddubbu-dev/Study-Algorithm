
from collections import deque

import sys
readline = lambda: sys.stdin.readline().strip()
# readline = input


N = int(readline())  # 1 ~ N

que = deque(range(1, N + 1))

while len(que) > 1:
    que.popleft()

    if len(que) > 1:
        num = que.popleft()
        que.append(num)


print(que[0])
