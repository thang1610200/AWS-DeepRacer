# Chương 4 - Kĩ thuật tối ưu code phần thưởng
## 4.1/Input Parameters of the AWS DeepRacer Reward Function
 + "all_wheels_on_track" (Boolean)  : cờ để cho biết tác nhân có đang trên đường đi

 + "x" (float ) : tọa độ x của tác nhân tính bằng mét

 + "y"  (float)  : tọa độ y của tác nhân tính bằng mét

 + "closest_objects"  [ int , int ] : chỉ số dựa trên số 0 của hai đối tượng gần nhất với vị trí hiện tại của tác nhân là (x, y).

 + "closest_waypoints"  [ int , int ] : chỉ số của hai điểm tham chiếu gần nhất.


 + "is_crashed"  (Boolean) :  Boolean cờ để cho biết tác nhân có bị rơi hay không.

 + "is_left_of_center" (Boolean)   :  Gắn cờ để cho biết nhân viên hỗ trợ có ở bên trái trung tâm đường đua hay không.

 + "is_offtrack"  (Boolean)  : Boolean cờ để cho biết tác nhân có đi chệch hướng hay không.

 + "is_reversed" (Boolean)  : để cho biết tác nhân đang lái theo chiều kim đồng hồ (Đúng) hay ngược chiều kim đồng hồ (Sai).

 + "heading" (float) :  đặc vụ ngáp theo độ
 
 + "objects_ distance" ([ float , ]) :  danh sách khoảng cách của các đối tượng tính bằng mét giữa 0 và track_length liên quan đến vạch xuất phát.

 + "objects_heading" ([ float , ] ) : danh sách các tiêu đề của đối tượng theo độ từ -180 đến 180.

 + "objects_left_of_center" ([ Boolean , ]) : danh sách các cờ Boolean cho biết đối tượng của các phần tử có nằm bên trái tâm hay không (Đúng ) hay không (Sai).

 + "objects_location"  [( float , float ),] : danh sách vị trí đối tượng [(x,y),...].


 + "progress" (float )  : phần trăm đường đua đã hoàn thành


 + "speed"  (float) : tốc độ của tác nhân tính bằng mét trên giây (m/s)

 + "steering_angle" (float)  : góc lái của tác nhân tính theo độ

 + "steps" (int) : số bước đã hoàn thành

 + "track_length" (float)  : chiều dài theo dõi tính bằng mét.

 + "track_width" (float )  : chiều rộng của rãnh
 
## 4.2/ Hyperparameters

Siêu tham số là các biến để kiểm soát quá trình đào tạo học tăng cường của bạn. Chúng có thể được điều chỉnh để tối ưu hóa thời gian đào tạo và hiệu suất mô hình của bạn.

Kỹ thuật tối ưu hóa mà AWS Deepracer sử dụng là PPO viết tắt của Proximal Policy Optimization. Để biết thêm về PPO, hãy sử dụng liên kết này PPO/OpenAI

Nhìn vào các tham số siêu khác nhau:

### 1.  Gradient descent batch size

Số lượng trải nghiệm phương tiện gần đây được lấy mẫu ngẫu nhiên từ bộ đệm trải nghiệm và được sử dụng để cập nhật các trọng số mạng thần kinh học sâu cơ bản. Lấy mẫu ngẫu nhiên giúp giảm các mối tương quan vốn có trong dữ liệu đầu vào. Sử dụng kích thước lô lớn hơn để thúc đẩy các bản cập nhật ổn định và mượt mà hơn cho các trọng số của mạng thần kinh, nhưng hãy lưu ý đến khả năng quá trình đào tạo có thể dài hơn hoặc chậm hơn.

Lô này là một tập hợp con của bộ đệm trải nghiệm bao gồm các hình ảnh do camera gắn trên phương tiện AWS DeepRacer ghi lại và các hành động mà phương tiện thực hiện.

### 2. Number of epochs

Số lần chuyển qua dữ liệu huấn luyện để cập nhật trọng số mạng thần kinh trong quá trình giảm dần độ dốc. Dữ liệu đào tạo tương ứng với các mẫu ngẫu nhiên từ bộ đệm trải nghiệm. Sử dụng số lượng kỷ nguyên lớn hơn để thúc đẩy các bản cập nhật ổn định hơn, nhưng mong đợi quá trình đào tạo chậm hơn. Khi kích thước lô nhỏ, bạn có thể sử dụng số lượng kỷ nguyên nhỏ hơn.

### 3. Learning rate

Trong mỗi lần cập nhật, một phần của trọng số mới có thể là từ đóng góp giảm độ dốc (hoặc tăng dần) và phần còn lại từ giá trị trọng số hiện có. Tốc độ học tập kiểm soát mức độ đóng góp của bản cập nhật giảm dần (hoặc tăng dần) vào trọng số mạng. Sử dụng tốc độ học tập cao hơn để bao gồm nhiều đóng góp giảm dần độ dốc để đào tạo nhanh hơn, nhưng hãy lưu ý khả năng phần thưởng mong đợi có thể không hội tụ nếu tốc độ học tập quá lớn.

### 4. Entropy

Mức độ không chắc chắn được sử dụng để xác định thời điểm thêm tính ngẫu nhiên vào phân phối chính sách. Tính không chắc chắn tăng thêm giúp phương tiện AWS DeepRacer khám phá không gian hành động rộng hơn. Giá trị entropy lớn hơn sẽ khuyến khích phương tiện khám phá không gian hành động kỹ lưỡng hơn.

### 5.  Discount factor

Hệ số chiết khấu xác định phần thưởng trong tương lai được chiết khấu bao nhiêu khi tính toán phần thưởng ở một trạng thái nhất định dưới dạng phần thưởng trung bình trên tất cả các trạng thái trong tương lai. Hệ số chiết khấu bằng 0 có nghĩa là trạng thái hiện tại không phụ thuộc vào các bước trong tương lai, trong khi hệ số chiết khấu 1 có nghĩa là bao gồm cả đóng góp từ tất cả các bước trong tương lai. Với hệ số chiết khấu là 0,9, phần thưởng dự kiến ​​ở một bước nhất định bao gồm phần thưởng từ đơn đặt hàng gồm 10 bước trong tương lai. Với hệ số chiết khấu là 0,999, phần thưởng dự kiến ​​bao gồm phần thưởng từ đơn đặt hàng 1000 bước trong tương lai.

### 6. Loss type

Loại hàm mục tiêu để cập nhật trọng số mạng. Một thuật toán đào tạo tốt sẽ thực hiện các thay đổi gia tăng đối với chiến lược của phương tiện để nó dần dần chuyển từ thực hiện các hành động ngẫu nhiên sang thực hiện các hành động chiến lược để tăng phần thưởng. Nhưng nếu nó tạo ra một thay đổi quá lớn thì quá trình đào tạo trở nên không ổn định và tác nhân sẽ không học được. Các loại tổn thất do lỗi bình phương Huber và Mean hoạt động tương tự đối với các bản cập nhật nhỏ. Nhưng khi các bản cập nhật trở nên lớn hơn, tổn thất Huber sẽ tăng nhỏ hơn so với tổn thất lỗi bình phương trung bình. Khi bạn gặp vấn đề về hội tụ, hãy sử dụng loại mất mát Huber. Khi hội tụ tốt và bạn muốn đào tạo nhanh hơn, hãy sử dụng loại tổn thất lỗi bình phương trung bình.

### 7. Number of experience episodes between each policy-updating iteration

Kích thước của bộ đệm trải nghiệm được sử dụng để lấy dữ liệu huấn luyện từ các trọng số mạng chính sách học tập. Đoạn đường là khoảng thời gian mà phương tiện xuất phát từ một điểm xuất phát nhất định và kết thúc là hoàn thành đường đua hoặc chệch khỏi đường đua. Các tập khác nhau có thể có độ dài khác nhau. Đối với các vấn đề học tăng cường đơn giản, một bộ đệm kinh nghiệm nhỏ có thể đủ và việc học sẽ nhanh chóng. Đối với các vấn đề phức tạp hơn có nhiều cực đại cục bộ hơn, bộ đệm kinh nghiệm lớn hơn là cần thiết để cung cấp nhiều điểm dữ liệu không tương quan hơn. Trong trường hợp này, đào tạo sẽ chậm hơn nhưng ổn định hơn. Các giá trị được khuyến nghị là 10, 20 và 40.

## 4.3/Waypoints Reward Function

## 4.4/Log Analysis 

## 4.5/ Một số code  phần thưởng tối ưu :
### Example 1: Đi theo đường trung tâm trong thử nghiệm thời gian
    def reward_function(params):
    '''
   Ví dụ về thưởng đi theo đường trung tâm
    '''

    //Đọc thông số đầu vào
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    //Tính 3 điểm đánh dấu ngày càng xa đường trung tâm
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    //Thưởng cao hơn nếu xe càng gần đường trung tâm và ngược lại
    if distance_from_center <= marker_1:
    reward = 1
    elif distance_from_center <= marker_2:
    reward = 0.5
    elif distance_from_center <= marker_3:
    reward = 0.1
    else:
    reward = 1e-3 # likely crashed/ close to off track
    return reward
### Example 2: Ở bên trong hai biên giới trong thử nghiệm thời gian
    def reward_function(params):
    '''
    Ví dụ về phần thưởng cho đại lý ở bên trong hai đường viền của đường đua
    '''

    // Đọc tham số đầu vào
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    // Đưa ra phần thưởng rất thấp theo mặc định
    reward = 1e-3
    // Trao phần thưởng cao nếu không có bánh nào chệch khỏi đường ray và
    // chiếc xe ở đâu đó giữa các đường viền
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
    reward = 1.0
    // Always return a float value
    return reward
### Example 3: Prevent Zig-Zag in Time Trials
    def reward_function(params):
    '''
    Ví dụ về chỉ đạo phạt, giúp giảm thiểu các hành vi sai
    '''

    // Đọc tham số đầu vào
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Chỉ cần góc lái tuyệt đối
    // Tính 3 điểm xa hơn và cha xa trung tâm hơn
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    // Phần thưởng cao hơn nếu xe càng gần đường trung tâm và ngược lại
    if distance_from_center <= marker_1:
    reward = 1.0
    elif distance_from_center <= marker_2:
    reward = 0.5
    elif distance_from_center <= marker_3:
    reward = 0.1
    else:
    reward = 1e-3 # likely crashed/ close to off track
    // Ngưỡng phạt lái, thay đổi số dựa trên cài đặt không gian hành động của bạn
    ABS_STEERING_THRESHOLD = 15
    // Thưởng phạt nếu xe bẻ lái quá nhiều
    if steering > ABS_STEERING_THRESHOLD:
    reward *= 0.8
    return float(reward)
### Example 4: Đi trên một làn đường mà không đâm vào chướng ngại vật cố định hoặc phương tiện đang di chuyển
    def reward_function(params):
    '''
    Ví dụ về thưởng cho đại lý ở bên trong hai biên giới
    và xử phạt khi đến quá gần các đối tượng phía trước
    '''
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    objects_distance = params['objects_distance']
    _, next_object_index = params['closest_objects']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']
    // Khởi tạo phần thưởng với một số nhỏ nhưng không phải bằng không
    //vì số không có nghĩa là lạc đường hoặc bị hỏng
    reward = 1e-3
    // Phần thưởng nếu đại lý ở bên trong hai đường viền của đường đua
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
    reward_lane = 1.0
    else:
    reward_lane = 1e-3
    
    // Phạt nếu tác tử ở quá gần đối tượng tiếp theo
    reward_avoid = 1.0
    // Khoảng cách đến đối tượng tiếp theo
    distance_closest_object = objects_distance[next_object_index]
    // Quyết định xem tác nhân và đối tượng tiếp theo có trên cùng một làn không
    is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center

    if is_same_lane:
    if 0.5 <= distance_closest_object < 0.8:
    reward_avoid *= 0.5
    elif 0.3 <= distance_closest_object < 0.5:
    reward_avoid *= 0.2
    elif distance_closest_object < 0.3:
    reward_avoid = 1e-3 # Likely crashed
    / Tính toán phần thưởng bằng cách đặt các trọng số khác nhau
    // hai khía cạnh trên
    reward += 1.0 * reward_lane + 4.0 * reward_avoid
    return reward
## 4.6/Một số model trainng có hiệu suất tốt
### EX1:
 <img src="img/r1.png">
    def reward_function(params):

    """
     Xác định chức năng khen thưởng dựa trên kế hoạch
     Chức năng này chỉ định ba cách để kiểm tra xem chúng ta nên thưởng hay phạt tác nhân đó. Đầu tiên, nó sẽ kiểm tra xem tất cả các bánh xe có đi đúng hướng hay không. Đại lý sẽ nhận được nhiều phần thưởng hơn bằng cách ở trong đường đua. Bất cứ khi nào bất kỳ bánh xe nào bị chệch hướng,  sẽ bị phạt 10 điểm. 

    Thứ hai, nó sẽ kiểm tra vị trí của tác nhân dựa trên các điểm tham chiếu. Vì đường dẫn mong muốn được chỉ định, đặt các thuộc tính của hàm phần thưởng. Đầu tiên,  chia các điểm tham chiếu thành ba mảng, trái, phải và trung tâm, dựa trên đường dẫn mong muốn. Sau khi đặt tất cả các điểm vào ba mảng này, chúng tôi xác định phần thưởng như sau:
    """
    center_variance = params["distance_from_center"] / params["track_width"]

    #racing line

    left_lane = [23,24,50,51,52,53,61,62,63,64,65,66,67,68]#Fill in the waypoints

   

    center_lane = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,26,27,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,54,55,56,57,58,59,60,69,70]#Fill in the waypoints

   

    right_lane = [29,30,31,32,33,34]#Fill in the waypoints

   

    #Speed :  kiểm tra tốc độ của tác nhân dựa trên các điểm tham chiếu

    fast = [0,1,2,3,4,5,6,7,8,9,25,26,27,28,29,30,31,32,51,52,53,54,61,62,63,64,65,66,67,68,69,70] #3

    moderate = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,55,56,57,58,59,60] #2

    slow = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] #1

 

    reward = 30

 

    if params["all_wheels_on_track"]:

        reward += 10

    else:

        reward -= 10

 

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:

        reward += 10

    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:

        reward += 10

    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:

        reward += 10

    else:

        reward -= 10

       

    if params["closest_waypoints"][1] in fast:

        if params["speed"] > 1.5 :

            reward += 10

        else:

            reward -= 10

    elif params["closest_waypoints"][1] in moderate:

        if params["speed"] > 1 and params["speed"] <= 1.5 :

            reward += 10

        else:

            reward -= 10

    elif params["closest_waypoints"][1] in slow:

        if params["speed"] <= 1 :

            reward += 10

        else:

            reward -= 10

       

   

    return float(reward)

### EX2: 
<img src="img/K123.png">
