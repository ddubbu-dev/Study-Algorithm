"""
Q. 일반적으로 sum 진행하면 안되는 이유는??
"""

from collections import deque
import sys
readline = lambda: sys.stdin.readline().strip()

K = int(readline())
stack = deque(maxlen=K)

for i in range(K):
    num = int(readline())

    if num == 0:
        try:
            stack.pop()
        except:  # 혹시나 맨 처음에 0이 나오면,
            continue
    else:
        stack.append(num)


print(sum(stack))
