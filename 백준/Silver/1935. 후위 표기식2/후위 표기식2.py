import sys

readline = lambda: sys.stdin.readline().strip()

from collections import deque

A_ASCII_INDEX = ord("A")
N = int(readline())
alpah_nums = [None] * 26
sentence = readline().rstrip()

for idx in range(N):
    num = int(readline())
    alpah_nums[idx] = num

stack = deque()
for s in sentence:
    if s not in ["*", "+", "-", "/"]:
        idx = ord(s) - A_ASCII_INDEX
        num = alpah_nums[idx]
        stack.append(num)
    else:
        a2 = stack.pop()
        a1 = stack.pop()

        if s == "*":
            stack.append(a1 * a2)
        elif s == "+":
            stack.append(a1 + a2)
        elif s == "-":
            stack.append(a1 - a2)
        else:
            stack.append(a1 / a2)

result = stack[0]
print(f"{result:.2f}")
