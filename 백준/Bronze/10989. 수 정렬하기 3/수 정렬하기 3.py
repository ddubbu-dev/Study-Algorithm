"""
[카운팅 정렬] ; O(N), O(N+K) ; K=최대값, 작을수록 좋음
나의 해석 : 말 그대로 개수를 세어 채우는 로직

[주의사항]
메모리 제한으로, input_arr, result_arr 따로 안 만듦
"""

import sys
def cinput():
    return sys.stdin.readline()

N = int(cinput())

# 최대값 (이미 주어짐)
maxV = 10000
count_arr = [0] * (maxV + 1)
    
# 개수세기
for _ in range(N):
    item = int(cinput())
    count_arr[item] += 1

# 정렬 마무리 
for item in range(maxV + 1):
    cnt = count_arr[item]
    for lap in range(cnt):
        # 메모리 초과로 바로 출력하기
        # result_arr.append(item)
        print(item)
        


