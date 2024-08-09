
import math

A, B, V = map(int, input().split())

"""
방법1) 수식
좋은점) 반복문 대비, 연산이 한번만 필요하니깐 더 효율적

distance = A - B

distance * (days-1) + A

"""
distance_per_day = A - B

days = math.ceil((V - A + distance_per_day) / distance_per_day)

print(days)


"""
방법2) 반복문
궁금한점) 10^9 이상 반복문을 돌경우 VSC 에서도 렉걸림, 이유가 뭘까?
"""
# days = 0 #총 일 수
# position = 0 #달팽이의 현재 위치

# while True:
    
#     print("position", position)
    
#     # 낮
#     days += 1 
#     position += A
    
#     if position >= V:
#         print(days)
#         break
    
#     # 밤
#     position -= B

