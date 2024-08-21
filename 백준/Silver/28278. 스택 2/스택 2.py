import sys

readline = lambda: sys.stdin.readline().strip()

from collections import deque

stack = deque()
N = int(readline())

for _ in range(N):
    nums = list(map(int, readline().split()))

    cmd = nums[0]
    try:
        if cmd == 1:
            stack.append(nums[1])
        elif cmd == 2:
            print(stack.pop())
        elif cmd == 3:
            print(len(stack))
        elif cmd == 4:
            print(1 if len(stack) == 0 else 0)
        elif cmd == 5:
            print(stack[-1])
    except:
        print("-1")