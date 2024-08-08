import sys

def cinput():
    return sys.stdin.readline()

"""
1. 숫자 뒤집기 (str화 > 잘라서 list화 > 뒤집기 > 합쳐서 str화 > 다시 int화)
2. A', B' 비교하기
"""

A, B = map(int, cinput().split())

reversed_A = int("".join(list(reversed(list(str(A))))))
reversed_B = int("".join(list(reversed(list(str(B))))))

maxV = max(reversed_A, reversed_B)

print(maxV)