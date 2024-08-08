import sys

def custom_input():
    return sys.stdin.readline()

A = int(custom_input())
B = int(custom_input())
B_3, B_2, B_1 = map(int, str(B))

"""
- 자리수별로 나누고 싶으면, str 자체를 int화
- 띄어쓰기로 적용하고 싶을때, str.split() == str.split(" ")
"""

print(A*B_1)
print(A*B_2)
print(A*B_3)
print(A*B)


