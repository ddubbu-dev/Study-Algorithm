
T = int(input())
arr = map(int, input().split())

"""
방법1) 반복문 돌면서, 약수인지 확인
"""

def isPrime(target):
    
    # 예외처리
    if target == 1:
        return False
    
    for i in range(2, target): #자기 미포함
        if target % i == 0:
            return False
        
    return True


cnt = 0

for item in arr:
    if isPrime(item):
        cnt += 1

print(cnt)