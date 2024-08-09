
N, M = map(int, input().split())
T = int(input())


# cut_point 만들기
# tip: (0,0), (M,N) 사전에 넣어주기
x_cut_points = [0, M]
y_cut_points = [0, N]

for i in range(T):
    is_y_cut_point, cut_point = map(int, input().split())
    
    if(is_y_cut_point):
        y_cut_points.append(cut_point)
    else:
        x_cut_points.append(cut_point)
        
# 정렬 후 자르기
x_cut_points.sort()
y_cut_points.sort()

# print(x_cut_points)
# print(y_cut_points)

# 최대 면적 구하기
max_area = 0
for x_i in range(1, len(x_cut_points)):
    for y_i in range(1, len(y_cut_points)):
        [x1, y1] = [x_cut_points[x_i-1], y_cut_points[y_i-1]]
        [x2, y2] = [x_cut_points[x_i], y_cut_points[y_i]]
        
        area = (x2 - x1) * (y2 - y1)
        
        # print("(%d, %d) ~ (%d, %d) = %d"%(x1, y1, x2, y2, area))
        
        if(area > max_area):
            max_area = area


print(max_area)