import sys

readline = lambda: sys.stdin.readline().strip()

while 1:
    num_str = readline()

    if num_str == "0":
        break

    length = len(num_str)

    is_pelin = True
    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            is_pelin = False
            break

    print("yes" if is_pelin else "no")
