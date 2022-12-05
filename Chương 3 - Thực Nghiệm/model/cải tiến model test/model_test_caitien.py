def reward_function(params):
    # đặt các giá trị đầu vào
    all_wheels_on_track = params['all_wheels_on_track']  # biến để kiểm tra xem xe có đang trên đường đua hay không
   # x = params['x'] # tọa độ x của xe
   # y = params['y'] #tọa độ y của xe
    distance_from_center = params['distance_from_center']  #khoảng cách giữa tâm của xe và tâm của đường đua
    #is_left_of_center = params['is_left_of_center'] # kiểm tra xem xe có ở trung tâm bên trái(true) đường đua hay 
                                                                                          #hay bên phải(false)                  
   # heading = params['heading'] # Hướng di chuyển của xe, tính theo độ
   # progress = params['progress'] #tỉ lệ phần trăm quãng đường mà xe đi được
   # steps = params['steps'] #Số bước mà xe đã hoàn thành
   # speed = params['speed'] #Tốc độ của xe (m/s)
    #steering_angle = params['steering_angle']   # Góc lái của xe (độ)
    track_width = params['track_width'] #chiều rộng của đường đua
    #waypoints = params['waypoints'] #Tọa độ (x,y) dọc theo trung tâm của đường đua
    #closest_waypoints = params['closest_waypoints'] #chỉ số của hai điểm waypoint gần xe nhất

    reward = 0

    # Xử phạt nếu xe đi ra ngoài đường đua
    if not all_wheels_on_track:
        print("off_track")
        return 1e-3 # Nếu mà đi ra ngoài đường đua xe trả về giá trị 10 ^-3


    # Đưa phần thưởng nhiều hơn nếu xe đi gần trung tâm đường đua
    distance_from_center_reward = 0
    # tạo 3 điểm đánh dấu 
    marker_1 = 0.1 * track_width    # Cách biên 1 khoảng cách marker_
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    if distance_from_center >= 0.0 and distance_from_center <= marker_1:# kiểm tra nếu khoảng cách từ tâm của xe đến tâm của đường đua lớn hơn or = 0 và nhỏ hơn bằng marker_1
        distance_from_center_reward = 1         # thì phần thưởng sẽ là 1
    elif distance_from_center <= marker_2:      ## mấy câu if sau có nghĩa là khoảng cách từ tâm xe đến tâm đường càng xa thì phần tưởng càng ít
        distance_from_center_reward = 0.8
    elif distance_from_center <= marker_3:
        distance_from_center_reward = 0.6
    else:
        return 1e-3

    print("distance_from_center_reward: %.2f" % distance_from_center_reward)
    reward = distance_from_center_reward

    print("total reward: %.2f" % reward)
    return float(reward)