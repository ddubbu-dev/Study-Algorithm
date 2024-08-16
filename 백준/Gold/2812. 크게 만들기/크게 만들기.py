
"""
[고민]
Q. 스택 자료구조여야만 하는 이유는? 
A. 6CK 면 사실 조합으로도 풀어도 될 것 같은디.. 고민되네

[아이디어] 
- stack bottom > top; 가장 큰수이므로 앞에 값들이 더 큼
"""

from collections import deque

import sys
readline = lambda: sys.stdin.readline().strip()
# readline = input

stack = deque()

N, K = map(int, input().split())
s_arr = list(map(int, list(input())))

for cur_val in s_arr:
    if len(stack) == 0:
        stack.append(cur_val)
        continue

    last_val = stack[-1]

    if K <= 0:
        stack.append(cur_val)
        continue

    if last_val >= cur_val:
        stack.append(cur_val)
    else:
        while K > 0:
            try:
                last_val = stack[-1]
                if cur_val > last_val:
                    stack.pop()
                    K -= 1
                else:
                    break
            except:
                break
        stack.append(cur_val)


for idx in range(len(stack) - K):  # 끝에 남은 K 만큼 잘라주어야함
    print(stack[idx], end="")