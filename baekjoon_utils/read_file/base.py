import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


A, B = map(int, input().split())
C, D = map(int, input().split())

print(A + B)
print(C + D)