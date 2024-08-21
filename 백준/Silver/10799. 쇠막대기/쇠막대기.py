"""
시간초과
- (x) 레이저 개수만 필요한거라 숫자로 치환해서 스택에 넣기; 이것도 이중 반복문이라 안됨
- (o) 레이저 개수를 따로 관리하고 초기화 시점 고민해보기

주요컨셉
- stack.push; 열린 괄호
- stack.pop; 닫힌 괄호
-- 바로 직전이 열린 괄호였다면, laser 커팅; +len(stack)
-- 단순 파이프 종료라면, +1

QnA
- #2504 괄호의값 문제랑 어떤 차이점이 있는거지?
"""


from collections import deque
import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input
arr = list(readline())

stack = deque()
answer = 0

laser_possible = True  # 연속으로 () 올 수 있는 가능성
for idx in range(len(arr)):
    s = arr[idx]
    if s == "(":
        laser_possible = True
        stack.append(s)
        continue
    elif s == ")":
        stack.pop()
        # find 레이저
        if laser_possible:
            answer += len(stack)
            laser_possible = False
            continue

        # find 쇠막대기 종료 및 리셋
        answer += 1
print(answer)
