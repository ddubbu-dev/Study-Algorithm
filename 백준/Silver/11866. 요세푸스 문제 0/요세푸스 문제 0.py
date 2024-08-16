"""
- (o) 심플하게 생각하기 >  꺼내서 해당 번째 수가 아니면 다시 넣기
- (x) 첫 고민;
Q. deque로 풀 수 없을 것 같음. 앞/뒤에서 꺼내는게 아니라 중간에서 연산이 반복됨
A. 순환큐? 무튼 그거로 구현해야할 듯
"""

from collections import deque

import sys
readline = lambda: sys.stdin.readline().strip()

N, K = map(int, readline().split())

que = deque(range(1, N + 1))

print("<", end="")
while len(que) >= 1:

    for i in range(K - 1):
        num = que.popleft()
        que.append(num)

    if len(que) == 1:
        print(que.popleft(), end="")
    else:
        print(que.popleft(), end=", ")

print(">")