# tạo cây và duyệt cây theo 3 cách inorder, preorder, postorder, levelorder, tìm số lượng nút, chiều cao của cây

from QueuesLinked import QueuesLinked  #


class _Node: # Định nghĩa lớp _Node để đại diện cho một nút trong cây nhị phân
    __slots__='_element','_left','_right'#để tối ưu hóa việc lưu trữ dữ liệu bằng cách chỉ định các thuộc tính được phép của đối tượng. Trong trường hợp này, các thuộc tính được phép bao gồm _element, _left, và _right.

    def __init__(self,element,left=None,right=None):#Hàm khởi tạo của lớp _Node với các tham số element, left, và right. Tham số left và right có giá trị mặc định là None.
        self._element=element #Gán giá trị của tham số element cho thuộc tính _element của đối tượng _Node.
        self._left=left    #Gán giá trị của tham số left cho thuộc tính _left của đối tượng _Node.
        self._right=right  #gán giá trị của tham số right cho thuộc tính _right của đối tượng _Node.

class BinaryTree: # Định nghĩa một lớp  BinaryTree.
    def __init__(self):# Định nghĩa hàm khởi tạo cho lớp BinaryTree
        self._root =None     # đặt self.root=None tức là cây lúc khởi tạo rỗng

    def maketree(self,e,left,right):# Định nghĩa một phương thức maketree cho lớp BinaryTree với ba tham số: e, left, và right.
        self._root = _Node(e,left._root,right._root)# Tạo một đối tượng _Node mới với các tham số e, left._root, và right._root, sau đó gán đối tượng này cho thuộc tính _root của đối tượng BinaryTree hiện tại.

    def inorder(self,troot): # hàm duyệt cây theo inoder( duyệt từ cây con bên trái cùng
        if troot: # kiểm tra nếu troot không phải là None
            self.inorder(troot._left) #duyệt từng nút con bên trái của một nút theo thứ tự trước và thực hiện đệ quy cho đến khi không còn nút con nào,trước khi tiếp tục duyệt nút con bên phải.)
            print(troot._element,end=' ')# in ra giá trị hiện tại
            self.inorder(troot._right)#cho đến khi không còn nút con nào, trước khi tiếp tục duyệt nút con bên phải
            # vì để print(troot._element,end=' ') ở dưới self.inoder(troot.left) nên sẽ duyệt đệ quy tới con bên trái cuối cùng trước
            # rồi duyệt từng bước lên nút gốc rồi duyệt qua mảng bên phải

    def preorder(self,troot): #hàm duyệt cây theo preoder (duyệt từng nút con bên trái của một nút theo thứ tự trước và thực hiện đệ quy cho đến khi không còn nút con nào, trước khi tiếp tục duyệt nút con bên phải.)
        if troot:# kiểm tra nếu troot không phải là None
            print(troot._element, end=' ') # in ra giá trị đang duyệt tới hiện tại
            self.preorder(troot._left) #duyệt từng nút con bên trái của một nút theo thứ tự trước và thực hiện đệ quy cho đến khi không còn nút con nào
            self.preorder(troot._right)#cho đến khi không còn nút con nào, trước khi tiếp tục duyệt nút con bên phải
            #vì lệnh print(troot._element, end=' ') để ở đầu nên sẽ duyệt từ gốc xuống từng cây con bên trái rồi in ra ,nếu cây con bên trái hết thì chuyển sang bên phải

    def postorder(self,troot):#hàm duyệt cây theo postoder (duyệt từng nút con bên trái của một nút theo thứ tự trước và thực hiện đệ quy cho đến khi không còn nút con nào, trước khi tiếp tục duyệt nút con bên phải.)
        if troot:# kiểm tra nếu troot không phải là None
            self.postorder(troot._left)#duyệt từng nút con bên trái của một nút theo thứ tự trước và thực hiện đệ quy cho đến khi không còn nút con nào
            self.postorder(troot._right)#cho đến khi không còn nút con nào, trước khi tiếp tục duyệt nút con bên phải
            print(troot._element, end=' ')# in ra giá trị đang duyệt tới hiện tại
            # vì print(troot._element, end=' ') để ở cuối cùng nên sẽ duyệt tới phần tử bên trái cùng bên mảng trái trước,rồi đến phần tử bên phải
            #duyệt đến phần tử gốc thì  duyệt cho đến phần tử bên trái cùng của mảng bên phải của gốc, rồi đến phần tử bên phải rồi từ từ duyệt đến gốc

    def levelorder(self): # duyệt theo mức level
        Q=QueuesLinked() # khởi tạo đối tượng Q từ lớp QueuesLinked
        t=self._root # gán t là root của cây
        print(t._element,end=' ') # in ra giá trị hiện tại
        Q.enqueue(t)   # thêm phần tử t vào cuối queues
        while not Q.isempty(): # chừng nào Q còn khác rỗng thì
            t= Q.dequeue()  # t gán cho  nút từ đầu hàng đợi Q
            if t._left: # nếu t có nút con bên trái thì
                print(t._left._element,end=' ') # in ra giá trị nút con bên trái
                Q.enqueue(t._left) # gán giá trị nút con bên trái vào cuối hàng đợi đ tiếp tục duyệt ở vòng lặp sau
            if t._right:#nếu t có nút con bên phải thì
                print(t._right._element, end=' ')# in ra giá trị nút con bên phải
                Q.enqueue(t._right)# gán giá trị nút con bên phải vào cuối hàng đợi đ tiếp tục duyệt ở vòng lặp sau

    def count(self,troot): # hàm đếm số lượng node của cây
        if troot: # nếu nút hiện tại có giá trị
            x=self.count(troot._left)
            y=self.count(troot._right)
            return x + y + 1 # đệ quy  để tính số lượng node của cây theo công thức x+y+1
        return 0

    def height(self,troot):# tính chiều cao của cây
        if troot: # nếu nút hiện tại không phải là None
            x=self.height(troot._left)# Đệ quy để tính chiều cao của cây con bên trái
            y=self.height(troot._right)# Đệ quy để tính chiều cao của cây con bên phải
            if x>y:
                return x+1  # Nếu chiều cao của cây con bên trái lớn hơn, trả về chiều cao của nó cộng thêm 1
            else:
                return y+1 # nếu không, trả về chiều cao của nó cộng thêm 1
        return 0

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t= BinaryTree()
a = BinaryTree()
x.maketree(40,a,a)
y.maketree(60,a,a)                                #               10
z.maketree(20,x,a)                               #               / \
r.maketree(50,a,y)                               #             20   30                  tạo ra cây như thế này
s.maketree(30,r,a)                             #             /      /
t.maketree(10,z,s)                            #            40       50
print("inorder traversal")                      #                        \
t.inorder(t._root)  # duyệt cây z theo inorder  #                         60
print()
print("preorder traversal")
t.preorder(t._root) # duyệt cây z theo preorder

print()
print("postorder traversal")
t.postorder(t._root)# duyệt cây z  theo postorder
print()

print ('level order traversal ')
t.levelorder()# duyệt cây theo levelorder
print()

print('number of nodes')# in ra số lượng nút của cây
print(t.count(t._root))

print('heigt')
print(t.height(t._root)-1) # in ra chiêu cao của cây



