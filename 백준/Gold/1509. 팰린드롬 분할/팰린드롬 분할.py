"""
참고한 풀이
- (기존) #10942 팰린드롬 여부
- (추가된 로직) https://thegreengables.tistory.com/m/16

TODO
- [Manacher's 알고리즘 점화식](https://steins-gate.tistory.com/174)

"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리
sentence = readline()
sentence = " " + sentence  # Q. 초기화, 반복문 범위가 어렵다.
N = len(sentence)

# dp[s][e] = s ~ e 까지 팰린드롬 여부
is_palindrome = [[False for _ in range(N)] for _ in range(N)]
for term in range(N):
    for s in range(N - term):
        e = s + term

        if s == e:
            is_palindrome[s][e] = True
        elif sentence[s] == sentence[e]:
            if e - s == 1:  # 길이 2
                is_palindrome[s][e] = True
            elif is_palindrome[s + 1][e - 1]:
                is_palindrome[s][e] = True

# dp[i] = i 까지 팰린드롬 분할 최소 수
dp = [0 for _ in range(N)]  # init, 모두 한글자씩 펠린드롬

for e in range(1, N):
    dp[e] = float("inf")  # 최소값 찾기 위한 init
    for s in range(1, e + 1):
        if is_palindrome[s][e]:
            dp[e] = min(dp[e], dp[s - 1] + 1)

print(dp[-1])
