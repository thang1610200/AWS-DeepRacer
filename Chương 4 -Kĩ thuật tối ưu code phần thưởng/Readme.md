# Chương 4 - Kĩ thuật tối ưu code phần thưởng
## 4.1/Input Parameters of the AWS DeepRacer Reward Function
{
 "all_wheels_on_track" : Boolean , # cờ để cho biết tác nhân có đang trên đường đi
 "x" : float , # tọa độ x của tác nhân tính bằng mét
 "y" : float , # tọa độ y của tác nhân tính bằng mét
 "closest_objects" : [ int , int ], # chỉ số dựa trên số 0 của hai đối tượng gần nhất với vị trí hiện tại của tác nhân là (x, y).
 "closest_waypoints" : [ int , int ], # chỉ số của hai điểm tham chiếu gần nhất.
 "khoảng_cách_từ_trung_tâm" : # khoảng cách tính bằng mét từ trung tâm đường đua
 "is_crashed" : Boolean , # Boolean cờ để cho biết tác nhân có bị rơi
hay không.
 "is_left_of_center" : Boolean , # Gắn cờ để cho biết nhân viên hỗ trợ có ở
bên trái trung tâm đường đua hay không.
 "is_offtrack" : Boolean , # Boolean cờ để cho biết tác nhân có đi chệ
ch hướng hay không.
 "is_reversed" : Boolean , cờ # để cho biết tác nhân đang lái theo chiều kim đồng hồ (Đúng) hay ngược chiều kim đồng hồ (Sai).
 "heading" : float , # đặc vụ ngáp theo độ
 "objects_ distance" [ float , ], # danh sách khoảng cách của các đối tượng tính bằng mét giữa 0 và track_length liên quan đến vạch xuất phát.
 "objects_heading" : [ float , ], # danh sách các tiêu đề của đối tượng theo độ từ -180 đến 180.
 "objects_left_of_center" : [ Boolean , ], # danh sách các cờ Boolean cho biết đối tượng của các phần tử có nằm bên trái tâm hay không (Đúng ) hay không (Sai).
 "objects_location" : [( float , float ),], # danh sách vị trí đối tượng [(x,y),...].
 "đối tượng_tốc độ" : ], # danh sách tốc độ của các đối tượng tính bằng mét trên giây.
 "progress" : float , # phần trăm đường đua đã hoàn thành
 "speed" : float , # tốc độ của tác nhân tính bằng mét trên giây (m/s)
 "steering_angle" : float , # góc lái của tác nhân tính theo độ
 "steps" : int , # số bước đã hoàn thành
 "track_length" : float , # chiều dài theo dõi tính bằng mét.
 "track_width" : float , # chiều rộng của rãnh
 "waypoints" : ), ] # danh sách (x,y) là cột mốc dọc theo trung tâm đường đua
}
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
### Example 1: Follow the Center Line in Time Trials
def reward_function(params):
 '''
 Example of rewarding the agent to follow center line
 '''

 //Read input parameters
 track_width = params['track_width']
 distance_from_center = params['distance_from_center']
 //Calculate 3 markers that are increasingly further away from the center line
 marker_1 = 0.1 * track_width
 marker_2 = 0.25 * track_width
 marker_3 = 0.5 * track_width
 // Give higher reward if the car is closer to center line and vice versa
 if distance_from_center <= marker_1:
 reward = 1
 elif distance_from_center <= marker_2:
 reward = 0.5
 elif distance_from_center <= marker_3:
 reward = 0.1
 else:
 reward = 1e-3 # likely crashed/ close to off track
 return reward
### Example 2: Stay Inside the Two Borders in Time Trials
def reward_function(params):
 '''
 Example of rewarding the agent to stay inside the two borders of the track
 '''

 // Read input parameters
 all_wheels_on_track = params['all_wheels_on_track']
 distance_from_center = params['distance_from_center']
 track_width = params['track_width']

 // Give a very low reward by default
 reward = 1e-3
 // Give a high reward if no wheels go off the track and
 // the car is somewhere in between the track borders
 if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
 reward = 1.0
 // Always return a float value
 return reward
### Example 3: Prevent Zig-Zag in Time Trials
def reward_function(params):
 '''
 Example of penalize steering, which helps mitigate zig-zag behaviors
 '''

 // Read input parameters
 distance_from_center = params['distance_from_center']
 track_width = params['track_width']
 steering = abs(params['steering_angle']) # Only need the absolute steering angle
 // Calculate 3 marks that are farther and father away from the center line
 marker_1 = 0.1 * track_width
 marker_2 = 0.25 * track_width
 marker_3 = 0.5 * track_width
 // Give higher reward if the car is closer to center line and vice versa
 if distance_from_center <= marker_1:
 reward = 1.0
 elif distance_from_center <= marker_2:
 reward = 0.5
 elif distance_from_center <= marker_3:
 reward = 0.1
 else:
 reward = 1e-3 # likely crashed/ close to off track
 // Steering penality threshold, change the number based on your action space setting
 ABS_STEERING_THRESHOLD = 15
 // Penalize reward if the car is steering too much
 if steering > ABS_STEERING_THRESHOLD:
 reward *= 0.8
 return float(reward)
### Example 4: Stay On One Lane without Crashing into Stationary Obstacles or Moving Vehicles
def reward_function(params):
 '''
 Example of rewarding the agent to stay inside two borders
 and penalizing getting too close to the objects in front
 '''
 all_wheels_on_track = params['all_wheels_on_track']
 distance_from_center = params['distance_from_center']
 track_width = params['track_width']
 objects_distance = params['objects_distance']
 _, next_object_index = params['closest_objects']
 objects_left_of_center = params['objects_left_of_center']
 is_left_of_center = params['is_left_of_center']
// Initialize reward with a small number but not zero
 //because zero means off-track or crashed
 reward = 1e-3
 // Reward if the agent stays inside the two borders of the track
 if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
 reward_lane = 1.0
 else:
 reward_lane = 1e-3
 // Penalize if the agent is too close to the next object
 reward_avoid = 1.0
 // Distance to the next object
 distance_closest_object = objects_distance[next_object_index]
 // Decide if the agent and the next object is on the same lane
 is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center

 if is_same_lane:
 if 0.5 <= distance_closest_object < 0.8:
 reward_avoid *= 0.5
 elif 0.3 <= distance_closest_object < 0.5:
 reward_avoid *= 0.2
 elif distance_closest_object < 0.3:
 reward_avoid = 1e-3 # Likely crashed
 # Calculate reward by putting different weights on
 # the two aspects above
 reward += 1.0 * reward_lane + 4.0 * reward_avoid
 return reward
