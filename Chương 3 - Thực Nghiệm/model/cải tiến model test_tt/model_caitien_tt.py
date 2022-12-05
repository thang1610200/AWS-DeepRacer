import math
def reward_function(params):  
    # Đọc các biến đầu vào
    waypoints = params['waypoints'] #Tọa độ (x,y) dọc theo trung tâm của đường đua
    closest_waypoints = params['closest_waypoints'] #chỉ số của hai điểm tham chiếu gần xe nhất
    heading = params['heading'] # Hướng di chuyển của xe, tính theo độ

    # Khởi tạo phần thưởng
    reward = 1.0

    # Tính hướng của đường trung tâm của đường đua 
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Tính hướng theo bán kính, dùng atan2 
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # đổi sang độ
    track_direction = math.degrees(track_direction)

    # Tính độ lệch giữa hướng theo dõi và hướng đi của xe
    direction_diff = abs(track_direction - heading)

    if direction_diff > 180:

        direction_diff = 360 - direction_diff

    # Phạt nếu chênh lệch quá lớn
    DIRECTION_THRESHOLD = 10.0

    if direction_diff > DIRECTION_THRESHOLD:

        reward *= 0.5

    return float(reward)