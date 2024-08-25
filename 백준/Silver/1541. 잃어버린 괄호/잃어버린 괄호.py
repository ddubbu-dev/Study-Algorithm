"""
[핵심 아이디어]
minus(-) 만나면 스택 끝내고 괄호 열기

[반례](https://www.acmicpc.net/board/view/133090)
- 틀린 이유: 누적합인데 acc에 할당해버림;
"""


import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

sentence = readline()

acc = 0
stack = []

last_operator = "+"
for s in sentence:
    if s in ["+", "-"]:  # 숫자화
        stack[-1] = int(stack[-1])

    if s == "+":
        continue
    if s == "-":
        if stack:  # 지금까지 숫자 덧셈
            stack = list(map(int, stack))
            if last_operator == "+":
                acc += sum(stack)
            else:
                acc -= sum(stack)

            stack.clear()
        last_operator = "-"

    else:
        if not stack:
            stack.append(s)
        else:
            if isinstance(stack[-1], str):
                stack[-1] = stack[-1] + s
            else:
                stack.append(s)

stack = list(map(int, stack))
remains = sum(stack)

if last_operator == "-":
    print(acc - remains)
else:
    print(acc + remains)