"""
[반례]
- 짝수개, 이미 펠린드롬문자열 : ABBA (expected; ABBA)
- 부분 팰린드롬 안될때, 뒤집고 하나 곂쳐서 출력 : ABCDBA (expedted; ABCDBABDCBA)


[시도2]
- 일치하면, 앞/뒤 포인터 가운데로 이동
- 다르면, 앞 글자 뒤에 추가하고 앞 포인터만 움직이기

[시도1]
- 앞N번째 = 뒤N번째 모든 자릿수 같으면, S 그 자체
- 하나라도 다르면 그냥 S + 역S (홀수면 S-1)
"""

import sys
readline = lambda: sys.stdin.readline().strip()

from collections import deque

N = int(readline())

for _ in range(N):
    word = readline()
    length = len(word)

    front_p = 0
    rear_p = length - 1

    is_pelin = True
    rear_p_move = 1
    while front_p < rear_p:
        if word[front_p] == word[rear_p]:
            rear_p -= 1
            rear_p_move += 1
        else:
            rear_p = length - 1
            rear_p_move = 1

            is_pelin = False

        front_p += 1

    sliced = list(word)[: front_p + 1]
    reversed = sliced[: length - rear_p_move]
    reversed.reverse()
    result = sliced + reversed

    if is_pelin:
        print("".join(word))
    else:
        print("".join(result))