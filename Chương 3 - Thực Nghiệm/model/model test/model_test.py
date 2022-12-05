# Hàm sẽ trả nhiều phần thưởng hơn nếu xe đi gân trung tâm của đường đua
def reward_function(params):

    # đặt các giá trị đầu vào
    all_wheels_on_track = params['all_wheels_on_track']  # biến để kiểm tra xem xe có đang trên đường đua hay không
   # x = params['x'] # tọa độ x của xe
   # y = params['y'] #tọa độ y của xe
    distance_from_center = params['distance_from_center']  #khoảng cách giữa tâm của xe và tâm của đường đua
    is_left_of_center = params['is_left_of_center'] # kiểm tra xem xe có ở trung tâm bên trái(true) đường đua hay 
                                                                                          #hay bên phải(false)                  
   # heading = params['heading'] # Hướng di chuyển của xe, tính theo độ
   # progress = params['progress'] #tỉ lệ phần trăm quãng đường mà xe đi được
   # steps = params['steps'] #Số bước mà xe đã hoàn thành
   # speed = params['speed'] #Tốc độ của xe (m/s)
    steering_angle = params['steering_angle']   # Góc lái của xe (độ)
    #track_width = params['track_width'] #chiều rộng của đường đua
    #waypoints = params['waypoints'] #Tọa độ (x,y) dọc theo trung tâm của đường đua
    #closest_waypoints = params['closest_waypoints'] #chỉ số của hai điểm waypoint gần xe nhất

    reward = 0


    # Xử phạt nếu xe đi ra ngoài đường đua
    if not all_wheels_on_track:
        print("off_track")
        return 1e-3 # Nếu mà đi ra ngoài đường đua xe trả về giá trị 10 ^-3

    #Góc lái âm thì xe quay sang trái, dương thì quay sang phải
    #Đoạn code này nhằm xác định xe phải ở trong đường đua thì mới được nhận thưởng
    steering_reward = 1e-3
    if distance_from_center > 0: #Nếu khoảng cách từ tâm của xe đến tâm của đường lớn hơn 0 thì
        if is_left_of_center and steering_angle >= 0: # nếu xe nằm ở bên trái trung tâm đường đua và góc lái của xe dương
            steering_reward = 1.0           #Gán steering_reward = 1.0
        elif (not is_left_of_center) and steering_angle <= 0:  # Nếu xe nằm bên phải và góc lái âm
            steering_reward = 1.0           #Gán steering_reward = 1.0
    else: #Nếu xe đi ngay giữa trung tâm đường đua thì
        if steering_angle == 0: #góc lái bằng 0 thì bánh xe luôn thẳng, tức là luôn đi giữa trung tâm đường đua        
            steering_reward = 1.0   # vì v phần thưởng sẽ đc gán là 1.0
    print("steering_reward: %.2f" % steering_reward)
    reward += steering_reward   # cộng tất cả steering_reward sẽ ra được phần thưởng

    print("total reward: %.2f" % reward)
    return float(reward)