def isPrime(target):
    
    # 예외처리
    if target == 1:
        return False
    
    elif target != 2 and target % 2 == 0:
        return False
    
    for i in range(2, target): #자기 미포함
        if target % i == 0:
            return False
        
    return True

T = int(input())

for i in range(T):
    num = int(input())
    
    """
    [tip]
    - 절반만 체크하면 될 듯
    - 역순으로 (차이가 작은 것부터 탐색하라 해서)
    """
    for A in range(num//2, 1, -1): # 반례) 2까지 포함해야함
        B = num - A
        
        if isPrime(A) and isPrime(B):
            print(A, B)
            break