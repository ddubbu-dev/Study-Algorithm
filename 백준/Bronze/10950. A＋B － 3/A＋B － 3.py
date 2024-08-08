import sys

def cinput():
    return sys.stdin.readline()

T = int(cinput())

for i in range(T):
    A, B = map(int, cinput().split())
    
    print(A+B)