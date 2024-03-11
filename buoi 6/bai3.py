class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def append(self, new_data):
      """
      Chèn một phần tử mới vào cuối danh sách liên kết.
      """
      new_node = Node(new_data)
      if self.head is None:
          # Nếu danh sách liên kết rỗng, phần tử mới trở thành đầu danh sách
          self.head = new_node
      else:
          # Nếu danh sách liên kết không rỗng, tìm đến cuối danh sách
          current = self.head
          while current.next:
              current = current.next
          # Thay đổi con trỏ của phần tử cuối cùng để trỏ đến phần tử mới
          current.next = new_node

  def display(self):
      """
      Hiển thị danh sách liên kết.
      """
      current = self.head
      while current:
          print(current.data, end=" -> ")
          current = current.next
      print("None")

# Ví dụ sử dụng
if __name__ == "__main__":
  linked_list = LinkedList()
  linked_list.append(2)
  linked_list.append(3)
  linked_list.append(4)
  linked_list.append(5)

  print("Danh sách liên kết ban đầu:")
  linked_list.display()

  new_element = 1
  linked_list.append(new_element)

  print("Danh sách liên kết sau khi chèn", new_element, "vào cuối:")
  linked_list.display()
