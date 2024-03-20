class _Node:
    # Giới hạn các thuộc tính mà một đối tượng _Node có thể chứa
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        # Hàm khởi tạo để tạo một đối tượng _Node với _element là giá trị và _next là con trỏ đến Node tiếp theo
        self._element = element 
        self._next = next


class QueuesLinked:
    def __init__(self):
        # Khởi tạo queue với _front và _rear là None, _size là 0
        self._front = None
        self._rear = None
        self._size = 0 
    
    def __len__(self):
        # Trả về độ dài (số lượng phần tử) của queue
        return self._size 

    def isempty(self):
        # Kiểm tra xem queue có trống không
        return self._size == 0

    def enqueue(self, e):
        # Thêm một phần tử vào cuối queue
        newest = _Node(e, None)
        if self.isempty():
            # Nếu queue trống, phần tử mới là cả _front và _rear
            self._front = newest
        else:
            # Ngược lại, liên kết phần tử mới với phần tử cuối cùng và cập nhật _rear
            self._rear._next = newest
        self._rear = newest
        self._size += 1 

    def dequeue(self):
        # Loại bỏ và trả về phần tử đầu tiên của queue
        if self.isempty():
            print('Queue is Empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            # Nếu queue rỗng sau khi loại bỏ, cập nhật cả _rear
            self._rear = None
        return e 

    def first(self):
        # Trả về giá trị của phần tử đầu tiên của queue
        if self.isempty():
            print('Queue is Empty')
            return 
        return self._front._element
    
    def display(self):
        # In ra nội dung của queue từ đầu đến cuối
        p = self._front
        while p:
            print(p._element, end='<--')
            p = p._next
        print()


# Tạo một đối tượng queue mới sử dụng lớp QueuesLinked
Q = QueuesLinked()

# Thêm các phần tử 5 và 3 vào cuối của queue
Q.enqueue(5)
Q.enqueue(3)

# Hiển thị nội dung của queue từ đầu đến cuối (Kết quả: 5 <-- 3 <--)
#Q.display()

# In ra độ dài (số lượng phần tử) của queue (Kết quả: Length 2)
#print('Length', len(Q))

# Thêm các phần tử 7 và 12 vào cuối của queue
Q.enqueue(7)
Q.enqueue(12)

# Hiển thị nội dung của queue sau khi thêm phần tử mới (Kết quả: 5 <-- 3 <-- 7 <-- 12 <--)
#Q.display()

# In ra độ lớn (số lượng phần tử) của queue sau khi thêm phần tử mới (Kết quả: Length 4)
#print('Length', len(Q))



            