###ĐỀ TÀI 19 : AWS Deep Racer ###

Thành viên: 
20110495 - Nguyễn Lê Huy 
20110568 - Nguyễn Hữu Thắng 
20110053 - Tô Duy Vượng 

1/Giới Thiệu:
Là xe mô hình tự hành đầu tiên được phát triển đặc biệt để giúp các nhà phát triển
làm quen với học tăng cường. AWS DeepRacer mang lại cho các nhà phát triển một
cách thức đơn giản để tìm hiểu RL, thử nghiệm các thuật toán RL mới và phương
thức chuyển nhượng tên miền từ mô phỏng đến thực tế, cũng như trải nghiệm RL
trong thế giới thực.
Chiếc xe đua tự hành được điều khiển bởi model học tăng cường, công cụ mô
phỏng đua xe 3D. Các nhà phát triển có thể huấn luyện, đánh giá và điều chỉnh các
mô hình RL trong công cụ mô phỏng trực tuyến, triển khai các mô hình của họ lên
AWS Deep Racer để có trải nghiệm xe tự hành trong thế giới thực và thi đấu trong
Giải đua AWS Deep Racer để có cơ hội giành Cúp vô địch AWS.
1/Chức năng đề tài
+Xây dựng mô hình cho các cuộc đua tránh vật thể .
+Đối đầu trực tiếp giữa hai xe bằng cách thử nghiệm với nhiều thông tin đầu vào từ
cảm biến, các thuật toán học tăng cường và cấu hình mạng nơ-ron mới nhất.

2/Các loại service cần thực hiện

+Amazon SageMaker : để huấn luyện model học tăng cường,
+ Amazon Kinesis Video Streams :để truyền phát video hậu trường mô phỏng ảo,
+Amazon S3 : để lưu trữ model .
+Amazon CloudWatch: để ghi nhật ký.
+Amazon Simple Storage Service: Lưu trữ model. + AWS Lambda: Tạo và chạy những thuật toán ‘thưởng’. + AWS CloudFormation: Tạo chế độ cho những models chạy. + AWS RoboMaker: Tạo ra môi trường để huấn luyện và thử nghiệm. -Dựa trên các container Robomaker và Sagemaker, hỗ trợ trên rất nhiều nền tảng thiết lập CPU và GPU. + Tập hợp rất nhiều kịch bản cho phép dễ dàng thiết kế model, không cần phải làm mọi thứ từ con số 0. + Cho phép các bản mẫu AWS Deep Racer từ nguồn khác; Cho phép tải lên mô hình đã được đào tạo sẵn.
-Bên cạnh đó, AWSDeepRacer còn giúp đỡ trong việc xây dựng model kể cả mô phỏng lẫn vật lý: + Giúp xây dựng một kết nối wifi dựa phương tiện AWS và AWS Deep Racer Console. + Có thể chỉnh sửa một số thông tin của phương tiện (tốc độ, độ cân bằng, các góc bánh xe) + Cũng đưa ra một số templates để xây dựng phương tiện cũng như đường đua vật lý để thử nghiệm ngoài đời thật -Bảo dữ liệu người dùng ngăn chặn những xe mô phỏng của mình có thể bị rò rỉ ra ngoài: + Dùng xác thực đa yếu tố(MFA) với mỗi người dùng mỗi lần đăng nhập. + Dùng SSL/TLS để truy xuất với dữ liệu của AWS. + Dùng API và lưu trữ thông tin người đăng nhập bằng AWS CloudTrail. + Dùng các cách bảo mật mã hóa.

 3/Thông tin khác Link github: 
 https://github.com/thang1610200/AWS-DeepRacer 
 Link video tìm hiểu đề tài: https://drive.google.com/drive/folders/19Lb5VbGQ8BAa8U2B5xgZsT37Mjysjbgi?usp= sharing