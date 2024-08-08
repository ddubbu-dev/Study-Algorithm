import sys

def cinput():
    return sys.stdin.readline().rstrip()


# 단순히 공백으로 분리하는 문제

line = cinput()
words = line.split()

print(len(words))