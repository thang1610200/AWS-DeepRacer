# Chương 1 - Giới thiệu về AWSDeepRacer
## 1.1/ Giới thiệu:
    AWS DeepRacer là phương pháp nhanh nhất (theo đúng nghĩa đen) để làm quen với công nghệ học tăng cường (RL), thông qua một chiếc xe đua tỷ lệ 1/18 tự hành hoàn toàn, được điều khiển bởi model học tăng cường, công cụ mô phỏng đua xe 3D và giải đua xe toàn cầu. Các nhà phát triển có thể huấn luyện, đánh giá và điều chỉnh các mô hình RL trong công cụ mô phỏng trực tuyến, triển khai các mô hình của họ lên AWS DeepRacer để có trải nghiệm xe tự hành trong thế giới thực và thi đấu trong Giải đua AWS DeepRacer để có cơ hội giành Cúp vô địch AWS DeepRacer.
    
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/gioithieu1.jfif" width = "400">
    <img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/gioithieu2.png" width = "400">
    <img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/gioithieu3.jfif" width = "400">
    <img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/gioithieu4.png" width = 400>
## 1.2/Các loại service cần thực hiện:
    Các dịch vụ của AWS mà AWS Deepracer sử dụng trực tiếp hoặc gián tiếp:
- Amazon Elastic Container Registry (Amazon ECR): + là sổ đăng ký bộ chứa được quản lý hoàn toàn, cung cấp dịch vụ lưu trữ hiệu suất cao để bạn có thể triển khai thành phần lạ và hình ảnh ứng dụng ở bất kỳ đâu một cách đáng tin cậy.
+ Được SageMaker gọi gián tiếp để tự động mở rộng quy mô hoạt động của nó.
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/AWS%20ECR.png" width = "400">

- AWS CloudFormation: + cho phép bạn lập mô hình, cung cấp và quản lý AWS cũng như các tài nguyên của bên thứ ba bằng cách xử lý cơ sở hạ tầng dưới dạng mã.
+ Được AWS DeepRacer gọi trực tiếp để tạo tài nguyên cho tài khoản.
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/AWS%20CloudFormation.png" width = "400">

-	Amazon CloudWatch: + thu thập và trực quan hóa bản ghi, chỉ số và dữ liệu sự kiện theo thời gian thực trong trang tổng quan tự động để hợp lý hóa cơ sở hạ tầng và bảo trì ứng dụng của bạn.
 + Được gọi trực tiếp bởi AWS DeepRacer để ghi nhật ký hoạt động của nó.
 + Được AWS RoboMaker, SageMaker gọi gián tiếp để ghi nhật ký hoạt động của nó.
 <img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/AWS%20CloudWatch.png" width = "400">

 -	Amazon EC2: + là nền tảng điện toán sâu rộng nhất, cùng với đó là hơn 500 phiên bản và tuyển tập bộ xử lý, dung lượng lưu trữ, kết nối mạng, hệ điều hành và mô hình mua hàng mới nhất để giúp bạn đáp ứng tốt nhất những nhu cầu về khối lượng công việc của mình.
+ Được AWS CloudFormation và SageMaker gọi gián tiếp để tạo và chạy các công việc đào tạo.


-	Amazon Kinesis Video Streams: + giúp cho việc truyền video theo cách bảo mật từ các thiết bị kết nối tới AWS dễ dàng hơn để phân tích, thực hiện machine learning (ML), phát lại và các phép xử lý khác.
+ Được AWS DeepRacer gọi trực tiếp để xem các luồng đào tạo đã lưu trong bộ nhớ cache.
+ Được AWS RoboMaker gọi gián tiếp vào các luồng đào tạo trong bộ nhớ cache.
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/AWS%20Kinesis%20video%20stream.png" width = "400">


-	AWS Lambda: + là một dịch vụ điện toán phi máy chủ, theo định hướng sự kiện, giúp bạn chạy mã cho hầu hết mọi loại ứng dụng hoặc dịch vụ backend mà không cần cung cấp hay quản lý máy chủ.
+ Được gọi trực tiếp bởi AWS DeepRacer để tạo và chạy các chức năng phần thưởng.
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/AWS%20Lambda.png" width = "400">


-	AWS RoboMaker: + là dịch vụ mô phỏng dựa trên đám mây, cho phép các nhà phát triển khoa học robot có thể chạy, thay đổi quy mô và tự động hóa tác vụ mô phỏng mà không cần quản lý bất kỳ cơ sở hạ tầng nào.
+ Được AWS DeepRacer gọi trực tiếp để kết xuất môi trường học tập tăng cường ảo trong mô phỏng.
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/RoboMaker.png" width = "400">


-	Amazon S3: + là một dịch vụ lưu trữ đối tượng cung cấp khả năng thay đổi quy mô, mức độ sẵn sàng của dữ liệu, độ bảo mật và hiệu suất hàng đầu trong ngành.
+ Được AWS RoboMaker gọi gián tiếp để liệt kê một nhóm bắt đầu bằng 
'deepracer' và để đọc các đối tượng trong nhóm hoặc ghi các đối tượng vào nhóm.
+ Được SageMaker gọi gián tiếp để thực hiện các hoạt động lưu trữ dành riêng cho SageMaker.
+ Được AWS DeepRacer gọi trực tiếp để tạo, liệt kê và xóa các bộ chứa có tên bắt đầu bằng " deepracer" Cũng được gọi để tải xuống các đối tượng từ nhóm, tải đối tượng lên nhóm hoặc xóa đối tượng khỏi nhóm.
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/AWS%20S3.png" width = "400">

-	Amazon SageMaker: +Xây dựng, đào tạo và triển khai các mô hình máy học (ML) cho bất kỳ trường hợp sử dụng nào với cơ sở hạ tầng, công cụ và quy trình công việc được quản lý đầy đủ.
+ Được gọi trực tiếp bởi AWS DeepRacer để huấn luyện các mô hình học tăng cường.


## 1.3/Hạn chế:
- Vì đây là mô phỏng không thể nắm bắt chính xác tất cả các khía cạnh của thế giới thực, do đó các mô hình được đào tạo về mô phỏng có thể không hoạt động tốt trong thế giới thực. Mô phỏng như vậy thường được gọi là khoảng cách hiệu suất mô phỏng-thực (sim2real).

## 1.4/Giải pháp khắc phục:
-	Để giúp giảm khoảng cách hiệu suất real2sim, hãy đảm bảo sử dụng màu sắc, hình dạng và kích thước giống nhau hoặc tương tự cho cả bản nhạc mô phỏng và bản nhạc thực. Hãy sử dụng các chướng ngại vật xung quanh đường đua thực. Ngoài ra, hãy hiệu chỉnh cẩn thận phạm vi tốc độ và góc lái của xe để không gian hành động được sử dụng trong huấn luyện phù hợp với thế giới thực. Đánh giá hiệu suất mô hình trong một đường mô phỏng khác với đường đua được sử dụng trong đào tạo có thể cho thấy mức độ chênh lệch hiệu suất thực tế.

## 1.5/Khái niệm Reinforment Learning (RL) :
-	Reinforcement Learning là việc đào tạo các mô hình Machine Learning để đưa ra một chuỗi các quyết định. Trong Reinforcement Learning, trí tuệ nhân tạo (AI) đối mặt với một tình huống giống như trò chơi. Máy tính sử dụng thử và sai (trial and error) để đưa ra giải pháp cho vấn đề. Để khiến máy làm những gì lập trình viên muốn, các máy (agent) sẽ nhận được phần thưởng (reward) hoặc hình phạt (penalty) cho những hành động(action) mà nó thực hiện. Mục tiêu của nó là tối đa hóa tổng phần thưởng.

## 1.6/ Ứng dụng 
•	Các thuật ngữ trong  Reinforcement Learning:
-	Environment (môi trường): là không gian mà máy tương tác.
-	Agent (máy): máy quan sát môi trường và sinh ra hành động tương ứng.
-	Policy (chiến thuật): máy sẽ theo chiến thuật như thế nào để đạt được mục đích.
-	Reward (phần thưởng): phần thưởng tương ứng từ môi trường mà máy nhận được khi thực hiện một hành động.
-	State (trạng thái): trạng thái của môi trường mà máy nhận được.
-	Episode (tập): một chuỗi các trạng thái và hành động cho đến trạng thái kết thúc.
•	Ứng dụng:
-	Trong quá trình học tăng cường, một agent, chẳng hạn như xe AWS DeepRacer thực hoặc ảo, với mục tiêu đạt được mục tiêu đã định sẽ tương tác với một environment để tối đa hóa tổng phần thưởng của agent. Agent thực hiện một hành động , được hướng dẫn bởi một chiến lược được gọi là policy , tại một trạng thái môi trường nhất định và đạt đến một trạng thái mới. Có một phần thưởng ngay lập tức liên quan đến bất kỳ hành động nào. Phần thưởng là thước đo mức độ mong muốn của hành động. Phần thưởng ngay lập tức này được coi là do môi trường trả lại.
-	Mục tiêu của quá trình học tăng cường trong AWS DeepRacer là tìm hiểu chính sách tối ưu trong một môi trường nhất định. Học tập là một quá trình lặp đi lặp lại các thử nghiệm và sai sót. Tác nhân thực hiện hành động ban đầu ngẫu nhiên để đến một trạng thái mới. Sau đó, tác nhân lặp lại bước từ trạng thái mới sang trạng thái tiếp theo. Theo thời gian, đại lý phát hiện ra các hành động dẫn đến phần thưởng dài hạn tối đa. Sự tương tác của tác nhân từ trạng thái ban đầu đến trạng thái kết thúc được gọi là một episode.

## 1.7/Một số các cuộc thi năm 2022
-	AWS DeepRacer League là giải đua xe tự lái toàn cầu đầu tiên trên thế giới dành cho các nhà phát triển. Xây dựng các mô hình máy học AWS DeepRacer và cạnh tranh trong giải vô địch toàn cầu, chạy đua giành giải thưởng, vinh quang và cơ hội nâng cao Cúp vô địch.
<img src = "https://github.com/thang1610200/AWS-DeepRacer/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20thi%E1%BB%87u%20v%E1%BB%81%20AWSDeepRacer/img/cuocthi.jfif" >

## 1.8/Thông tin khác Link github: 
- Link video tìm hiểu đề tài: https://drive.google.com/drive/folders/19Lb5VbGQ8BAa8U2B5xgZsT37Mjysjbgi?usp= sharing