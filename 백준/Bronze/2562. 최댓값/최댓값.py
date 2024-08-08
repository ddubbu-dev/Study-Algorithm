import sys

def cinput():
    return sys.stdin.readline()

N = 9

A = []

for i in range(N):
    num = int(cinput())
    A.append(num)

# 최댓값 구하기
sorted_A = sorted(A)
max_val = max(sorted_A)
print(max_val)

# 최댓값 출력
for i in range(N):
    if max_val == A[i]:
        print(i+1) # 서수니깐,
        break

