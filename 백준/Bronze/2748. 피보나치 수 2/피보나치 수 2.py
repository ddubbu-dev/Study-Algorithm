import sys

readline = lambda: sys.stdin.readline()
# readline = input

MAX_N = 90
TMP_VALUE = -1
memo = [0, 1] + [TMP_VALUE] * MAX_N


def recur(n):
    if memo[n] != TMP_VALUE:
        return memo[n]

    result1 = recur(n - 1)
    result2 = recur(n - 2)
    memo[n - 1] = result1
    memo[n - 2] = result2

    return result1 + result2


N = int(readline())
print(recur(N))