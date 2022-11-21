
# Chương 2. Xây dựng mô hình.

## 2.1/Điều chỉnh mô hình ( cấu hình các chức năng xe đua)?

## 2.2/Cấu hình model ?

## 2.3/Một số thuật toán  traiing  đã cải tiến ?

## 2.4/Cách đánh giá hiệu suất model ?

## 2.5/Các yếu tố ảnh hưởng  đến hiệu suất model ?

## 2.6/Quy trình xây dựng  model ?
Để đánh giá một mô hình được đào tạo trong bảng điều khiển AWS DeepRacer
### B1/ Từ ngăn điều hướng chính, chọn   Your Model rồi chọn mô hình bạn vừa đào tạo từ danh sách Mô hình để mở trang chi tiết mô hình.
### B2/ Chọn Evaluation tab
### B3/  Evaluation details ->   Start evaluation
<img src="img/e1.png">
Bạn có thể bắt đầu đánh giá sau khi trạng thái công việc đào tạo của bạn thay đổi thành Completed   hoặc trạng thái của mô hình thay đổi thành  Ready nếu công việc đào tạo chưa hoàn thành.
Một mô hình đã sẵn sàng khi công việc đào tạo hoàn tất. Nếu quá trình đào tạo chưa hoàn thành, mô hình cũng có thể ở trạng thái Sẵn sàng nếu nó được đào tạo đến điểm không thành công.
### B4/ Trên trang Evaluate model , bên dưới Evaluate criteria , nhập tên cho đánh giá của bạn, sau đó chọn loại cuộc đua mà bạn đã chọn để đào tạo mô hình.
<img src="img/e5.png">
Để đánh giá, bạn có thể chọn loại đường đua khác với loại đường đua được sử dụng trong huấn luyện. Ví dụ: bạn có thể đào tạo một mô hình cho các cuộc đua đối đầu với bot và sau đó đánh giá mô hình đó để thử nghiệm theo thời gian. Nói chung, mô hình phải khái quát hóa tốt nếu loại cuộc đua đào tạo khác với loại cuộc đua đánh giá. Đối với lần chạy đầu tiên, bạn nên sử dụng cùng một loại cuộc đua để đánh giá và huấn luyện.
Bạn có thể chọn bất kỳ đường chạy nào để đánh giá mô hình của mình, tuy nhiên, bạn có thể mong đợi hiệu suất tốt nhất trên đường chạy gần giống nhất với đường chạy được sử dụng trong đào tạo.
Để xem mô hình của bạn có khái quát hóa tốt hay không, hãy chọn một bản đánh giá khác với bản được sử dụng trong đào tạo.

### B5/ Trên trang Evaluate model, bên dưới  Virtual Race Submission, đối với mô hình đầu tiên của bạn, hãy tắt tùy chọn Submit model after evaluation. Sau này, nếu bạn muốn tham gia một sự kiện đua xe, hãy bật tùy chọn này.
<img src="img/e6.png">
### B6/ Trên trang Evaluate model , chọn  Start evaluation để bắt đầu tạo và khởi tạo công việc đánh giá.
Quá trình khởi tạo này mất khoảng 3 phút để hoàn thành.
 ### B7/Khi quá trình đánh giá diễn ra, kết quả đánh giá, bao gồm thời gian dùng thử và tỷ lệ hoàn thành đường đua, được hiển thị dưới phần chi tiết đánh giá sau mỗi lần thử. Trong cửa sổ Simulation video stream , bạn có thể xem tác nhân thực hiện như thế nào trên đường đã chọn.

Bạn có thể dừng một công việc đánh giá trước khi nó hoàn thành. Để dừng công việc đánh giá, hãy chọn Stop evaluation ở góc trên bên phải của  Evaluation rồi xác nhận để dừng đánh giá.

 ### B8/  Sau khi công việc đánh giá hoàn tất, hãy kiểm tra chỉ số hiệu suất của tất cả các thử nghiệm trong Evaluation results. . Luồng video mô phỏng đi kèm không còn nữa.
 <img src="img/e10.png">
 Lịch sử đánh giá mô hình của bạn có sẵn trong  Evaluation selector . Để xem chi tiết của một đánh giá cụ thể, hãy chọn đánh giá từ Evaluation selector , sau đó chọn Load evaluation  từ góc trên cùng bên phải của Evaluation selector .
 Đối với công việc đánh giá cụ thể này, mô hình được đào tạo sẽ hoàn thành các thử nghiệm với một hình phạt đáng kể về thời gian không theo dõi. Lần chạy đầu tiên, điều này không có gì lạ. Các lý do có thể bao gồm việc đào tạo không hội tụ và đào tạo cần nhiều thời gian hơn, không gian hành động cần được mở rộng để cung cấp cho nhân viên nhiều chỗ hơn để phản ứng hoặc chức năng phần thưởng cần được cập nhật để xử lý các môi trường khác nhau.
Bạn có thể tiếp tục cải thiện mô hình bằng cách sao chép mô hình đã được đào tạo trước đó, sửa đổi chức năng phần thưởng, điều chỉnh siêu tham số, sau đó lặp lại quy trình cho đến khi tổng phần thưởng hội tụ và chỉ số hiệu suất được cải thiện. Để biết thêm thông tin về cách cải thiện quá trình đào tạo, hãy xem Đào tạo và đánh giá các mô hình AWS DeepRacer.
Để chuyển mô hình được đào tạo hoàn chỉnh của bạn sang phương tiện AWS DeepRacer để lái trong môi trường thực tế, bạn cần tải xuống các thành phần lạ của mô hình. Để làm như vậy, hãy chọn Tải xuống mô hình trên trang chi tiết của mô hình. Nếu phương tiện vật lý AWS DeepRacer của bạn không hỗ trợ cảm biến mới và mô hình của bạn đã được huấn luyện với các loại cảm biến mới, thì bạn sẽ nhận được thông báo lỗi khi sử dụng mô hình trên phương tiện AWS DeepRacer của mình trong môi trường thế giới thực. Để biết thêm thông tin về thử nghiệm mô hình AWS DeepRacer với tác nhân vật lý, xem Vận hành phương tiện AWS DeepRacer của bạn.