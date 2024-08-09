
num_str = input().rstrip()

def is한수(target_str):
    if len(target_str) < 3:
        return True
    
    digit = list(map(int, target_str))
    
    # 주의사항 : 절댓값이 아니라, 차이만큼 -/+ 변화분 유지
    evenly_distance = digit[0] - digit[1] 
    for i in range(len(digit)-1):
        digit_i = digit[i]
        digit_j = digit[i+1]
        
        if digit_i - digit_j != evenly_distance:
            return False
        
    return True


cnt = 0
for target in range(1, int(num_str)+1):
    if is한수(str(target)):
        cnt +=1
        
        
print(cnt)