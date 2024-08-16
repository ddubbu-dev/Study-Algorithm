
"""
[아이디어] 
- ( : append
- ) : pop

짝이 맞으면 valid
- pop 할수 있으면
- 다 끝나고 남은게 없으면
"""

from collections import deque
import sys
readline = lambda: sys.stdin.readline().strip()

T = int(readline())
stack = deque()

for idx in range(T):
    s_arr = list(readline())
    is_valid = True

    for s in s_arr:
        if s == "(":
            stack.append(1)
        else:
            try:
                stack.pop()
            except:
                is_valid = False
                break
    if len(stack) == 0 and is_valid:
        print("YES")
    else:
        print("NO")

    stack.clear()
