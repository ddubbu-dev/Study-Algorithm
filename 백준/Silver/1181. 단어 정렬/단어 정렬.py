import sys

def input():
    return sys.stdin.readline()

"""
꿀팁
- lambda 함수는 익명으로 선언하고 싶을때, 
- 하지만 함수 조건이 복잡할 경우 이렇게 tuple 로 우선순위를 넘겨주면 될 듯하다
"""
def compare(item):
    return (len(item), item)

N = int(input())
arr = []

for i in range(N):
    line = input().rstrip()
    if not line in arr:
        arr.append(line)

arr.sort(key=compare)

for item in arr:
    print(item)