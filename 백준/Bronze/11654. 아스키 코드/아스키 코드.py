import sys

def cinput():
    # int화 안할 수 있으니 항상 개행문자 버려주기
    return sys.stdin.readline().rstrip() 

c = cinput()

print(ord(c)) #반대는 chr