class Queue:
    def __init__(self):
        self.s1 = []  # Stack 1 để lưu trữ các phần tử mới
        self.s2 = []  # Stack 2 để lưu trữ các phần tử cũ

    def enqueue(self, item):
        # Thêm phần tử mới vào stack 1
        self.s1.append(item)

    def dequeue(self):
        # Nếu stack 2 rỗng, di chuyển tất cả các phần tử từ stack 1 sang stack 2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        # Lấy phần tử đầu tiên từ stack 2
        return self.s2.pop()

    def is_empty(self):
        # Kiểm tra xem cả hai stack đều rỗng hay không
        return not self.s1 and not self.s2
