import sys

def cinput():
    return sys.stdin.readline()

A = int(cinput())
B = int(cinput())
C = int(cinput())

result_num = A * B * C

cnt_arr = [0] * 10 # 0 ~ 9

result_str = str(result_num) 
for i in range(len(result_str)):
    key = int(result_str[i])
    cnt_arr[key] = cnt_arr[key] + 1
    
for i in range(len(cnt_arr)):
    print(cnt_arr[i])