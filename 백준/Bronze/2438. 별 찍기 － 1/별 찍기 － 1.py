import sys

def cinput():
    return sys.stdin.readline()

N = int(cinput())

for i in range(1, N+1):
    print("*"*i)