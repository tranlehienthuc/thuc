from collections import defaultdict
#sử dụng class defaultdict là lớp con của dict có sẵn trong module collections cho phép bạn thiết lập một giá trị mặc định cho các khóa mới được truy cập mà không cần phải kiểm tra xem khóa đó đã tồn tại trong dictionary chưa.
# Khởi tạo defaultdict với giá trị mặc định là list
d = defaultdict(list)

# Thêm phần tử vào khóa 'key1'
d['key1'].append(1)
print(d)  # defaultdict(<class 'list'>, {'key1': [1]})

# Truy cập vào khóa 'key2' chưa tồn tại
print(d['key2'])  # []
print(d)  # defaultdict(<class 'list'>, {'key1': [1], 'key2': []})
