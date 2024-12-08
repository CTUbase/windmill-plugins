# Windmill Plugins

Tập hợp những plugin được phát triển cho nền tảng Windmill, phục vụ cho **cuộc thi Phần mềm nguồn mở - Olympic Tin học Sinh viên Việt Nam 2024**.

## 📃 Danh sách Plugin

### 1. **Mô hình 1: Trích xuất những địa điểm gặp nguy hiểm từ VNExpress**

#### Miêu tả:
Plugin này có chức năng:
- Crawl dữ liệu từ trang tìm kiếm của VNExpress.
- Lọc các URL của những bài báo liên quan đến các trường hợp nguy hiểm (thiên tai, bệnh dịch).
- Trích xuất các địa điểm được đề cập trong những bài báo này.

#### Ứng dụng:
Công cụ hữu ích để cảnh báo các khu vực nguy hiểm, hỗ trợ ra quyết định nhanh chóng trong quản lý khẩn cấp.

#### Truy cập Plugin:
[Predicting the Extent of Natural Disasters - GitHub](https://hub.windmill.dev/scripts/github/9891/predicting-the-extent-of-natural-disasters-github)

---

### 2. **Mô hình 2: Dự đoán mức độ nghiêm trọng của sự kiện**

#### Miêu tả:
Plugin này sử dụng các thông tin mô tả cụ thể về thiệt hại, như:
- Số người thiệt mạng.
- Số người bị thương.
- Thiệt hại về tài sản.

Từ đó, plugin phân tích và đưa ra dự đoán về **mức độ nghiêm trọng của sự kiện** với các cấp độ:

- **Mức độ 0**: Không gây nhiều thiệt hại, mức độ khẩn cấp thấp.
- **Mức độ 1**: Thiệt hại nhẹ về người và tài sản, mức độ khẩn cấp trung bình.
- **Mức độ 2**: Thiệt hại khá cao, mức độ khẩn cấp cao, cần hỗ trợ kịp thời.
- **Mức độ 3**: Thiệt hại lớn, đời sống bị ảnh hưởng nghiêm trọng, mức độ khẩn cấp rất cao.

#### Ứng dụng:
Giúp các tổ chức đánh giá mức độ khẩn cấp của sự kiện, từ đó ưu tiên nguồn lực hỗ trợ.

#### Truy cập Plugin:
[Flow Suggests Disaster Locations - Windmill Hub](https://hub.windmill.dev/flows/57/flow-suggests-disaster-locations)

---

## 🔧 Hướng dẫn cài đặt và sử dụng

### 1. Đối với phiên bản Windmill Cloud:
#### Bước 1: Đăng nhập vào Windmill: https://app.windmill.dev/
#### Bước 2: Tạo workspace tương ứng
#### Bước 3: Truy cập vào đường link dẫn đến hub 
#### Bước 4: Chọn "Edit/Run in Windmill", trang web sẽ tự động tạo một bản sao để bạn có thể tùy chỉnh và sử dụng trong workspace của bạn 

### 2. Đối với phiên bản Windmill Self-host:
#### Yêu cầu: cài đặt Windmill CLI tại [Hướng dẫn cài đặt Windmill CLI](https://www.windmill.dev/docs/advanced/cli)
#### Bước 1: Clone repo về máy tính
`git clone https://github.com/CTUbase/windmill-plugins.git`
#### Bước 2: Thêm workspace của bạn (nếu chưa có)
`wmill workspace add <tên workspace> <url workspace>`
#### Bước 3: Pull workspace về thư mục trên máy tính. Sau khi thực hiện, bạn sẽ thấy thư mục f (folder).
`wmill sync pull`
#### Bước 3: Sao chép thư mục "windmill_plugins" trong repo vào trong thư mục f vừa được tạo
#### Bước 4: Push những thay đổi lên workspace, lúc này bạn có thể thấy hai model xuất hiện trong workspace để dễ dàng sử dụng
`wmill sync push`

## 🤝 Đóng góp
- Nếu bạn có bất kỳ đóng góp nào, hãy mở Pull Request hoặc Issue trên GitHub của dự án.

## ⚖️ Giấy phép
- MIT-0 lisences

---

## 📞 Liên hệ
- **Tác giả**: CTUbase
- **Email**: hoangphuc090104@gmail.com

---


