"""
Q1. 단순히 library 를 쓸 수 있는가?
Q2. 알고리즘을 공부하므로, 직접 구현해본다면 어떤 알고리즘을?
"""
import sys
def cinput():
    return sys.stdin.readline()

N = int(cinput())
arr = []

for i in range(N):
    item = int(cinput())
    arr.append(item)
    
arr = sorted(arr)

for item in arr:
    print(item)

