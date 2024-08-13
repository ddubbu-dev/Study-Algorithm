
"""
[문제 이해]
- (x) 이분탐색 이라면, 가장 큰 값 10억, 사정거리(L)를 target으로 둬야하는거 아냐?
-- L은 상수, O(M*N) = O(10^10), 즉 M, N 중이 target 으로 둬야함
-- 1D, M을 우선 target으로

[최종 로직]
- binary search target; hunter 위치
- condition; distance <= 4
"""

M, N, L = map(int, input().split())
hunters = list(map(int, input().split()))
hunters.sort()

animals = []  # 잡으면 False 처리
for _ in range(N):
    animals.append(list(map(int, input().split())))


def get_distance(x, a, b):
    return abs(x - a) + b


catched_animal_cnt = 0


def meet_hunters(animal_idx):
    global catched_animal_cnt

    animal_pos = animals[animal_idx]
    animal_x = animal_pos[0]
    animal_y = animal_pos[1]
    # print(f"animal_pos={animal_pos}")

    start_idx = 0
    end_idx = len(hunters) - 1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        hunter_pos = hunters[mid_idx]

        d = get_distance(hunter_pos, animal_x, animal_y)
        if d <= L:
            # print(f"catched!! by hunter={hunter_pos}\n")
            catched_animal_cnt += 1
            animals[animal_idx] = False
            return

        # distance--
        if animal_x < hunter_pos:  # distance--, 왼쪽으로
            end_idx = mid_idx - 1
        elif animal_x > hunter_pos:
            start_idx = mid_idx + 1
        else:  # 더 이상 해 없음; d > L, start_idx=mid_idx 탐색 끝
            # print("놓침")
            return


for animal_idx in range(len(animals)):
    meet_hunters(animal_idx)

print(catched_animal_cnt)
