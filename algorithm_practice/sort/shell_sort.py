def set_open(input_):
    class open:
        def __init__(self, x):
            self.read = lambda: input_

        def __iter__(self):
            return iter(input_.split("\n"))

    return open


def set_input(input_):
    return iter(input_.split("\n")).__next__


input = set_input(
    """8
    7
    4
    6
    5
    8
    3
    2
    1"""
)


### /////// 아래부터 제출 영역 ///////

"""
Shell정렬

1. 등장 배경
Insertion정렬의 
- 장점(일부 정렬되었을 경우, 속도가 아주 빠름)은 살리고,
- 단점(삽입할 위치가 멀리 떨어져 있을 경우 이동 횟수가 많아짐)을 보완

좀 더 쉬운 설명
- 배열 뒷부분의 작은 숫자를 앞부분으로 빠르게 이동시키고
동시에 앞부분의 큰 숫자는 뒷부분으로 이동시킴

2. 방법
- 비교할 요소 그룹핑; by gap; gap = size//2 = #sub리스트
- sub리스트 간에 삽입정렬로 정렬; size=1 될때까지 반복

3. 시간 복잡도
- 쉘 정렬의 수행 속도는 간격 선정이 중요
- 가장 좋은 성능을 보이는 간격은 1, 4, 10, 23, 57, 132, 301, 701 (미발견)
    ㄴ Q. 테스트 필요
- 이 때문에 쉘 정렬의 시간복잡도 또한 아직 풀리지 않은 문제로 남아있다.
- O(N^1.25)
    ㄴ 계산되는 원리 리서치 필요
"""


class CompareCnt:
    def __init__(self):
        self.compare_cnt = 0  # 연산 횟수 비교

    def increase_cnt(self):
        self.compare_cnt += 1

    def get_cnt(self):
        return self.compare_cnt


IS_DEV = True


def print_only_dev(value):
    if IS_DEV:
        return print(value)
    else:

        def temp():
            return

        return temp


def print_arr_item(title, arr, compare_cnt):

    for item in arr:
        print(item)

    print_only_dev(f"[{title}] swap 횟수: {compare_cnt.get_cnt()}")
    print_only_dev(f"-----------------\n\n")


def swap(arr, from_idx, to_idx, compare_cnt):  # -> None

    temp = arr[from_idx]
    arr[from_idx] = arr[to_idx]
    arr[to_idx] = temp

    compare_cnt.increase_cnt()


def insertion_sort(x, compare_cnt, start=0, gap=1):
    arr = x[:]
    for target_idx in range(start + gap, len(arr), gap):
        for j in range(target_idx, 0, -1):  # 뒤에서부터 삽입할 곳 찾기
            print_only_dev(f"{arr[j-1]} vs {arr[j]}")

            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1, compare_cnt)
            else:
                break

        print_only_dev(f"=> idx={target_idx}까지 정렬 완료 {arr}\n")
    return arr


def shell_sort(x, compare_cnt):

    arr = x[:]
    gap = len(arr) // 2

    sub_group_num = 1
    while gap > 0:
        print_only_dev(f"=========#sub_group:{sub_group_num}(gap={gap}) 시작=========")
        for point in range(0, len(arr) - gap):
            # sub리스트 순회

            tmp = arr[point + gap]
            while True:
                if point < 0:
                    print_only_dev(f"clear")
                    break
                if arr[point] < arr[point + gap]:
                    # insertion sort 에서처럼, 뒤=>앞 넣을 곳 탐색
                    # 혹 넣을 곳 찾았다면, stop

                    # TODO: sub_list 출력값으로 표현해보자

                    print_only_dev(f"{arr} point={point} | {arr[point]} vs {tmp}")
                    break

                print_only_dev(f"{arr} point={point} | {arr[point]} vs {tmp} (swap)")

                # arr[point + gap] = arr[point]
                swap(arr, point, point + gap, compare_cnt)
                point -= gap  # Q. 왜 빼주나? A. sub리스트(gap간격으로 이동) 구조에서 insertion 비교하기 위해
            arr[point + gap] = tmp  # Q

        print_only_dev(f"=========#sub_group:{sub_group_num}(gap={gap}) 끝=========")
        gap = gap // 2
        sub_group_num += 1

    return arr


def shell_sort_simple(x):
    arr = x[:]
    gap = len(arr) // 2

    while gap > 0:
        for right_point in range(gap, len(arr)):
            idx_left = right_point - gap

            tmp = arr[right_point]

            point = idx_left

            while point >= 0 and arr[point] > tmp:
                arr[point + gap] = arr[point]
                point -= gap
            arr[point + gap] = tmp

            print(f"{arr} << {arr[idx_left]} vs {arr[idx_left + gap]}")

        gap = gap // 2

    return arr


# =============== 함수 정의 끝 ===============

T = int(input())
arr = []

for i in range(T):
    num = int(input())
    arr.append(num)

print_only_dev("<<<<<<<<<<<<<<< insertionSort >>>>>>>>>>>>>>>")
print_only_dev(f"원본 {arr}\n")
insertion_compare_cnt = CompareCnt()
insertion_sorted_arr = insertion_sort(arr, insertion_compare_cnt, 0, 1)
print_arr_item("insertion", insertion_sorted_arr, insertion_compare_cnt)

print_only_dev("<<<<<<<<<<<<<<< shellSort >>>>>>>>>>>>>>>")
print_only_dev(f"원본 {arr}\n")
shell_compare_cnt = CompareCnt()
shell_sorted_arr = shell_sort(arr, shell_compare_cnt)  # shell_sort_simple(arr)
print_arr_item("shell", shell_sorted_arr, shell_compare_cnt)
