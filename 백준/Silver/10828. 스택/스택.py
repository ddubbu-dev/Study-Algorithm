import sys
from collections import deque

#input = 

T = int(sys.stdin.readline())

stack = deque() #, maxlen=T

for i in range(T):
    cmds = sys.stdin.readline()
    try:
        cmd, num = cmds.split()
        num = int(num)
    except:
        cmd = cmds.strip()

    if cmd == "push":
        stack.append(num)
    elif cmd == "pop":
        try:
            print(stack.pop())
        except:
            print("-1")
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif cmd == "top":
        try:
            print(stack[-1])
        except:
            print("-1")
