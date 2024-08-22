"""
10:05 ~10:21

[아이디어]
문자열폭발처럼, PPAP 만나면 제거??

[시간초과]
- SLICE 하면 N^2 > 뒤에서부터 지우는 과정으로
"""


import sys

sys.setrecursionlimit(10**6)
readline = lambda: sys.stdin.readline().strip()
# readline = input  # TODO: 백준 제출 시 제거하기


line = readline()
bomb = "PPAP"
len_bomb = len(bomb)

stack = []
for s in line:
    stack.append(s)
    last_str = "".join(stack[len(stack) - len_bomb :])

    if last_str == bomb:  # 뒤에거 지우기
        for _ in range(len_bomb):
            stack.pop()

        stack.append("P")


result = "".join(stack)

if result == bomb or result == "P":
    print("PPAP")
else:
    print("NP")