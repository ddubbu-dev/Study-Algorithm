"""
- 동료 코드 리뷰 후 안보고 작성해봄
- 하지만, 추후 재풀이 필요
"""

from collections import deque
import sys
readline = lambda: sys.stdin.readline().rstrip()
# readline = input

s_arr = list(readline())
stack = deque()

try:
    for s in s_arr:
        if s in ["(", "["]:
            stack.append(s)
        elif s == ")":
            tmp = 0
            while True:
                last_s = stack.pop()
                if last_s == "(":
                    if tmp == 0:
                        stack.append(2)
                    else:
                        stack.append(tmp * 2)
                    break
                elif isinstance(last_s, int):
                    tmp += last_s
                else:
                    raise 0
        else:  # s == "]"
            tmp = 0
            while True:
                last_s = stack.pop()
                if last_s == "[":
                    if tmp == 0:
                        stack.append(3)
                    else:
                        stack.append(tmp * 3)
                    break
                elif isinstance(last_s, int):
                    tmp += last_s
                else:
                    raise 0

    print(sum(stack))

except:
    print(0)
