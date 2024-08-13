"""
[참고자료](https://jyeonnyang2.tistory.com/279)
[핵심 로직]
- 설치수(cnt) ↑, 공유기 간 인접거리(distance) ↑
- cnt:condition, distance:mid (=binary search 타겟)
"""

import sys

N, C = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()  # 필수; binary search는 정렬이 필수

# distance; binary search 타겟
left = 1  # cnt=N; 모든 집에 설치되어있다는 가정
right = arr[-1] - arr[0]  # cnt=2; 양 끝 집에만 설치되어있다는 가정

best_distance = 0  # 학습; 뭔가 딥러닝 같아

while left <= right:

    distance = (left + right) // 2

    # 첫번째 집에 기본으로 설치
    cur = arr[0]
    cnt = 1

    # 설치 가능 체크
    for i in range(1, N):
        if arr[i] >= cur + distance:
            # 다음집(arr[i])이 현재집(cur)과 distance 이상의 거리를 가짐
            cnt += 1
            cur = arr[i]

    if cnt >= C:
        # condition에 부합하고, 최적의 distance이면 저장
        if best_distance < distance:
            best_distance = distance

        # cnt ↓, distance ↑
        left = distance + 1  # distance가 길어지는 방향으로 움직이기

    else:
        # cnt ↑, distance ↓
        right = distance - 1


print(best_distance)
