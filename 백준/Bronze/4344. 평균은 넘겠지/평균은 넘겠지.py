import sys

def cinput():
    return sys.stdin.readline()

C = int(cinput())

for i in range(C):
    arr = list(map(int, cinput().split())) # map to list
    N = arr.pop(0) #0번째 아이템 꺼내기
    avg_val = sum(arr)/N
    
    cnt = 0
    for i in range(N):
        score = arr[i]
        if score > avg_val:
            cnt += 1
    ratio= cnt/N * 100
    
    print('%.3f'%(ratio) + "%")
    