def reward_function(params):

    
    # Đọc thông số đầu vào
    distance_from_center = params['distance_from_center']

    track_width = params['track_width']

  

    all_wheels_on_track = params['all_wheels_on_track']

    speed = params['speed']

    SPEED_THRESHOLD = 1

 

    # tính  5 điểm khoảng cách bắt  tính từ  vạch trung tâm

    marker_1 = 0.1 * track_width

    marker_2 = 0.20 * track_width

    marker_3 = 0.30 * track_width

    marker_4 = 0.40 * track_width

    marker_5 = 0.5 * track_width

 

    # Cho phần thưởng cao hơn nếu xe gần đường trung tâm hơn

    if distance_from_center <= marker_1 and all_wheels_on_track:

        reward = 3.0

    elif distance_from_center <= marker_2 and all_wheels_on_track:

        reward = 2.5

    elif distance_from_center <= marker_3 and all_wheels_on_track:

        reward = 1.5

    elif distance_from_center <= marker_4 and all_wheels_on_track:

        reward = 1

    elif distance_from_center <= marker_5 and all_wheels_on_track:

        reward = 0.5

    else:

        reward = 1e-3  # đánh dấu  xe đi lệch hướng

   


    if speed < SPEED_THRESHOLD:

        # Đưa ra hình phạt nếu xe chạy chậm

        reward = reward + 0.5

    else:

        # Thưởng với điều kiện xe đi đúng hướng và nhanh

        reward = reward + 1.0
    
    return float(reward)