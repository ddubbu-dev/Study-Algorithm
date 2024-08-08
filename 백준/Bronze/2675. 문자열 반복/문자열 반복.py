import sys

def cinput():
    return sys.stdin.readline()

T = int(cinput())

for i in range(T):
    N, word = cinput().split()
    N = int(N)

    for i in range(len(word)):
        c = word[i]
        print(c*N,end="")
    print() #개행