
"""
[문제 이해]
- NxN
- 같은 색으로 칠해져 있지 않으면, (N/2)x(N/2)
- 모두 같은색일경우 stop
- print_only_dev(#잘라진 하얀 색종이), print_only_dev(#잘라진 파란 색종이)

"""


def print_only_dev(args):
    printable = False
    if printable:
        return print(args)


WHITE_COLOR = "WHITE"
BLUE_COLOR = "BLUE"
MIXED = "MIXED"


def check_color_mode(arr):
    size = len(arr)

    color_code = arr[0][0]

    for i in range(size):
        for j in range(size):
            if not color_code == arr[i][j]:
                return MIXED

    if color_code == 0:
        return WHITE_COLOR
    else:
        return BLUE_COLOR


white_paper = 0
blue_paper = 0


def dfs(arr):
    global white_paper, blue_paper

    if len(arr) == 0:
        return

    color_mode = check_color_mode(arr)

    if color_mode == WHITE_COLOR:
        print_only_dev(f">> {color_mode}{arr}")
        white_paper += 1
        return
    elif color_mode == BLUE_COLOR:
        print_only_dev(f">> {color_mode}{arr}")
        blue_paper += 1
        return
    else:
        size = len(arr)
        half_size = size // 2
        print_only_dev(f"============{half_size}============")

        sub_list_scope = [
            [[0, half_size], [0, half_size]],
            [[0, half_size], [half_size, size]],
            [[half_size, size], [0, half_size]],
            [[half_size, size], [half_size, size]],
        ]

        for scope in sub_list_scope:
            [start_range, end_range] = scope
            sub_list = []
            for i in range(start_range[0], start_range[1]):
                sub_list.append(arr[i][end_range[0] : end_range[1]])

            print_only_dev(f"scope {start_range} ~ {end_range} >> {sub_list}")
            dfs(sub_list)


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dfs(arr)


print(f"{white_paper}\n{blue_paper}")
