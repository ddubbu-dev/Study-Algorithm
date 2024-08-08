import sys

def custom_input():
    return sys.stdin.readline().rstrip()

[A, B] = map(int, custom_input().split()) #str to int

print(A+B)
print(A-B)
print(A*B)
print(A//B) #몫 주의
print(A%B)
