import sys
def cinput():
    return sys.stdin.readline().rstrip()

N = int(cinput())

for i in range(N):
    score = 0
    prev_s =""
    seq_times = 1
    
    line = cinput()
    for j in range(len(line)):
        cur_s = line[j]
        if cur_s == "O":
            if cur_s == prev_s:
                seq_times += 1
                score += seq_times
                # print(seq_times, end=" + ")
            else:
                score += 1
                # print("1 + ", end=" + ")
        else: #초기화
            seq_times = 1
        prev_s = cur_s

    print(score)
