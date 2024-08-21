import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

from collections import deque

line = readline()
tmp_word = deque()
is_tag_name = False


def print_word(tmp_word: list[str], is_tag_name: bool):
    if not is_tag_name:
        tmp_word.reverse()

    print("".join(tmp_word), end="")

    return []  # 초기화


for s in line:
    if s in [" ", ">"]:
        tmp_word = print_word(tmp_word, is_tag_name)
        if s == ">":
            is_tag_name = False
    elif s == "<":
        tmp_word = print_word(tmp_word, is_tag_name)
        is_tag_name = True
    else:
        tmp_word.append(s)
        continue

    print(s, end="")

if tmp_word:
    tmp_word = print_word(tmp_word, False)
