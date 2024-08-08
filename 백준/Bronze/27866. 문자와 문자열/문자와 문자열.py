import sys

def custom_input():
    return sys.stdin.readline()

S = custom_input()
i = int(custom_input())

print(S[i-1])