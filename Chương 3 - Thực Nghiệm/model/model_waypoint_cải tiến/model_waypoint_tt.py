import math
import numpy as np
def reward_function(params):

    # gán các tham số 
    FUTURE_STEP = 7
    MID_STEP = 4
    TURN_THRESHOLD = 10     # độ
    DIST_THRESHOLD = 1.2    # m
    SPEED_THRESHOLD = 1.8   # m/s

    # Các tham số đầu vào
    all_wheels_on_track = params['all_wheels_on_track'] # biến để kiểm tra xem xe có đang trên đường đua hay không
    closest_waypoints = params['closest_waypoints'] #chỉ số của hai điểm tham chiếu gần xe nhất
    distance_from_center = params['distance_from_center']   #khoảng cách giữa tâm của xe và tâm của đường đua
    is_offtrack = params['is_offtrack'] #biến để kiểm tra xem xe có đi chệch hướng hay ko
    progress = params['progress'] ##tỉ lệ phần trăm quãng đường mà xe đi được
    speed = params['speed']#Tốc độ của xe (m/s)
    steps = params['steps'] #Số bước mà xe đã hoàn thành
    track_width = params['track_width'] #chiều rộng của đường đua
    waypoints = params['waypoints'] #Tọa độ (x,y) dọc theo trung tâm của đường đua

    # Hàm này dùng để xác định có khúc cua phía trước hay không
    def identify_corner(waypoints, closest_waypoints, future_step):

        # Tính hướng dõi của xe hiện tại 
        point_prev = waypoints[closest_waypoints[0]]
        point_next = waypoints[closest_waypoints[1]]

        # Tính hướng theo dõi của xe trong tương lai (xem khoảng cách 7 bước tiếp theo)
        point_future = waypoints[min(len(waypoints) - 1, 
                                     closest_waypoints[1] + future_step)]

        # Góc độ hiện tại của xe so với đường đua
        heading_current = math.degrees(math.atan2(point_prev[1] - point_next[1], 
                                                 point_prev[0] - point_next[0]))


        # # Góc độ tương lai của xe so với đường đua
        heading_future = math.degrees(math.atan2(point_prev[1] - point_future[1], 
                                                 point_prev[0]-point_future[0]))

        # tính độ lệch giữa hiện tại và tương lai
        diff_heading = abs(heading_current - heading_future)

        if diff_heading > 180:
            diff_heading = 360 - diff_heading

        # Tính khoảng cách đến điểm tham chiếu xa hơn
        dist_future = np.linalg.norm([point_next[0] - point_future[0],
                                      point_next[1] - point_future[1]])  

        return diff_heading, dist_future

    # lựa chọn tốc độ phù hợp với mỗi quãng đường
    def select_speed(waypoints, closest_waypoints, future_step, mid_step):

        # lấy 2 giá trị trả về của hàm identify_corner khoảng cách là 7 bước
        diff_heading, dist_future = identify_corner(waypoints, 
                                                    closest_waypoints, 
                                                    future_step)

        #Nếu độ lệch nhỏ hơn 10 độ
        if diff_heading < TURN_THRESHOLD:
            # thì sẽ đi nhanh hơn
            go_fast = True
        else:
            if dist_future < DIST_THRESHOLD: # Nếu xem 1.2 m có khúc cua nào không
                # Nếu có một góc cua và nó gần sẽ đi chậm hơn
                go_fast = False
            else:
                # lấy 2 giá trị trả về của hàm identify_corner khoảng cách là 4 bước
                diff_heading_mid, dist_mid = identify_corner(waypoints, 
                                                             closest_waypoints, 
                                                             mid_step)
               # #Nếu độ lệch nhỏ hơn 10 độ
                if diff_heading_mid < TURN_THRESHOLD:
                    # Nếu không có góc cua sẽ đi nhanh
                    go_fast = True
                else:
                    # Nếu có một góc cua và nó gần sẽ đi chậm hơn
                    go_fast = False

        return go_fast

    # Nếu xe ko trong đường đua or lệch hướng
    if not all_wheels_on_track or is_offtrack:
        reward = 1e-3  
        return float(reward)
    
    # Thưởng càng cao nếu xe càng gần vạch giữa và ngược lại
     # 0 nếu đang ở rìa đường đua, 1 nếu ở giữa đường đua
    reward = 1 - (distance_from_center/(track_width/2))**(1/4) + progress/steps

    go_fast = select_speed(waypoints, closest_waypoints, FUTURE_STEP, MID_STEP)

    if go_fast and speed > SPEED_THRESHOLD:
        reward += 0.5

    elif not go_fast and speed < SPEED_THRESHOLD:
        reward += 0.5    
      
    return float(reward)