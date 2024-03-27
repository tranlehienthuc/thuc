class Node:
    def __init__(self, he_so, so_mu):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    def them_so_hang(self, he_so, so_mu):
        new_node = Node(he_so, so_mu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ke_tiep:
                current = current.ke_tiep
            current.ke_tiep = new_node

    def rut_gon(self):
        current = self.head
        while current:
            temp = current.ke_tiep
            while temp:
                if temp.so_mu == current.so_mu:
                    current.he_so += temp.he_so
                    current.ke_tiep = temp.ke_tiep
                temp = temp.ke_tiep
            if current.he_so == 0:
                current = current.ke_tiep
            else:
                current = current.ke_tiep

    def tich(self, other):
        result = DaThuc()
        current1 = self.head
        while current1:
            current2 = other.head
            while current2:
                result.them_so_hang(current1.he_so * current2.he_so, current1.so_mu + current2.so_mu)
                current2 = current2.ke_tiep
            current1 = current1.ke_tiep

        result.rut_gon()
        return result

    def in_da_thuc(self):
        current = self.head
        while current:
            print(f"{current.he_so}x^{current.so_mu}", end=" ")
            current = current.ke_tiep
        print()

dathuc1 = DaThuc()
dathuc1.them_so_hang(3, 2)
dathuc1.them_so_hang(-2, 3)
dathuc1.them_so_hang(5, 2)

dathuc2 = DaThuc()
dathuc2.them_so_hang(1, 1)
dathuc2.them_so_hang(-4, 0)

print("Đa thức 1:")
dathuc1.in_da_thuc()

print("Đa thức 2:")
dathuc2.in_da_thuc()

dathuc3 = dathuc1.tich(dathuc2)

print("Đa thức kết quả:")
dathuc3.in_da_thuc()