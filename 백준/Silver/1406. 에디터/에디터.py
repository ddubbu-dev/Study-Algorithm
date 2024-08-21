"""
[아이디어]
- 파일 텍스트가 스택? stack[-1] 오른쪽; 현재 커서 위치
- 커서 위치가 바뀐다고 앞/뒤 문자가 삭제되는게 아닐 거 같은데
- L; stack[-1] 꺼내서 tmp_str 누적
- R; push tmp_str[0]
- B; pop
- P $; push $
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

from collections import deque

init_line = readline()
cmd_cnt = int(readline())

left = deque(list(init_line))
right = deque()

for _ in range(cmd_cnt):
    cmds = readline().split()

    if cmds[0] == "L":
        if left:
            right.appendleft(left.pop())
    elif cmds[0] == "D":
        if right:
            left.append(right.popleft())
    elif cmds[0] == "B":
        if left:
            left.pop()
    elif cmds[0] == "P":
        s = cmds[1]
        left.append(s)


result = left + right
print("".join(result))