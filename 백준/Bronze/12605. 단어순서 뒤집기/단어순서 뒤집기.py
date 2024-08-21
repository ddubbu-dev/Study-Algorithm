import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

from collections import deque

T = int(readline())

for case in range(1, T + 1):
    words = readline().split()
    words.reverse()
    print(f"Case #{case}: {' '.join(words)}")
